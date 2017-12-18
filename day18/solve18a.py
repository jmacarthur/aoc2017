#!/usr/bin/python

import sys

with open(sys.argv[1], "rt") as f:
    instructions = [x.strip().split(" ") for x in f.readlines()]

registers = [0]*26
pc = 0
sound_freq = 0
while True:
    instruction = instructions[pc]
    first_reg = None
    first_val = None
    second_val = None
    if instruction[1].isalpha():
        first_reg = ord(instruction[1]) - ord('a')
        first_val = registers[first_reg]
    else:
        first_val = int(instruction[1])
    if len(instruction)>2:
        if instruction[2].isalpha():
            second_val = registers[ord(instruction[2]) - ord('a')]
        else:
            second_val = int(instruction[2])
    print("%3.3d %s %s [%d]    %d"%(pc, instruction[0], instruction[1], first_val, second_val or 0))
    if instruction[0] == 'set':
        registers[first_reg] = second_val
    elif instruction[0] == 'mul':
        registers[first_reg] *= second_val
    elif instruction[0] == 'mod':
        registers[first_reg] %= second_val
    elif instruction[0] == 'add':
        registers[first_reg] += second_val
    elif instruction[0] == 'snd':
        sound_freq = first_val
    elif instruction[0] == 'jgz':
        # Subtract one to account for the automatic increment later
        if first_val > 0: pc += second_val - 1
    elif instruction[0] == 'rcv':
        if first_val != 0:
            recovered_val = sound_freq
            break
    pc += 1

print("Recovered value: %d\n"%recovered_val)
