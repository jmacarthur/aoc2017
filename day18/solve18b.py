#!/usr/bin/python

import sys

with open(sys.argv[1], "rt") as f:
    instructions = [x.strip().split(" ") for x in f.readlines()]

class CPUState(object):
    def __init__(self, inqueue, outqueue, cpuid):
        self.registers = [0]*26
        self.registers[ord('p') - ord('a')] = cpuid
        self.pc = 0
        self.sound_freq = 0
        self.inqueue = inqueue
        self.outqueue = outqueue
        self.sendcount = 0
        self.cpuid = cpuid

def run_cpu(cpustate):
    instruction = instructions[cpustate.pc]
    first_reg = None
    first_val = None
    second_val = None
    if instruction[1].isalpha():
        first_reg = ord(instruction[1]) - ord('a')
        first_val = cpustate.registers[first_reg]
    else:
        first_val = int(instruction[1])
    if len(instruction)>2:
        if instruction[2].isalpha():
            second_val = cpustate.registers[ord(instruction[2]) - ord('a')]
        else:
            second_val = int(instruction[2])
    print("%s(%d) %3.3d %s %s [%d]    %d"%(" "*40*cpustate.cpuid, cpustate.cpuid, cpustate.pc,
                                           instruction[0], instruction[1], first_val, second_val or 0))
    if instruction[0] == 'set':
        cpustate.registers[first_reg] = second_val
    elif instruction[0] == 'mul':
        cpustate.registers[first_reg] *= second_val
    elif instruction[0] == 'mod':
        cpustate.registers[first_reg] %= second_val
    elif instruction[0] == 'add':
        cpustate.registers[first_reg] += second_val
    elif instruction[0] == 'snd':
        cpustate.outqueue.append(first_val)
        cpustate.sendcount += 1
    elif instruction[0] == 'jgz':
        # Subtract one to account for the automatic increment later
        if first_val > 0: cpustate.pc += second_val - 1
    elif instruction[0] == 'rcv':
        if len(cpustate.inqueue)==0:
            return True # Deadlocked; do not increment PC
        else:
            cpustate.registers[first_reg] = cpustate.inqueue.pop(0)
    cpustate.pc += 1
    return False


cpu_1_to_2 = []
cpu_2_to_1 = []

cpu0 = CPUState(cpu_2_to_1, cpu_1_to_2, 0)
cpu1 = CPUState(cpu_1_to_2, cpu_2_to_1, 1)

while True:
    terminate_0 = run_cpu(cpu0)
    terminate_1 = run_cpu(cpu1)
    if terminate_0 and terminate_1: break
    
print("Halted after CPU 1 sent %d values" % cpu1.sendcount);
