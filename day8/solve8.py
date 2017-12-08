#!/usr/bin/env python

import sys # for 'exit'

registers = {}

def ensure_reg(reg_name):
    global registers
    """ Creates a register in the global register file, set to zero, if one does not exist already exist. """
    if reg_name in registers: return
    else: registers[reg_name] = 0

def comparison_passes(a, comparison, b):
    if comparison == '<': return a < b
    elif comparison == '>': return a > b
    elif comparison == '>=': return a >= b
    elif comparison == '<=': return a <= b
    elif comparison == '!=': return a != b
    elif comparison == '==': return a == b
    else:
        print("Unknown comparison: '%s'"%comparison)
        sys.exit(0)

highest_val = 0        
f = open("input8.txt", "rt")
while True:
    l = f.readline().strip()
    if l == "": break
    (update_reg, action, amount, _, condition_reg, condition, compare_val) = l.split()
    amount = int(amount)
    compare_val = int(compare_val)
    ensure_reg(update_reg)
    ensure_reg(condition_reg)
    if action == "dec": amount = -amount
    elif action == "inc": pass
    else:
        print("Action '%s' is unknown!"%(action))
        break
    res = comparison_passes(registers[condition_reg], condition, compare_val)
    print("> %s"%l)
    print("inc by %d if %d %s %d (%s)"%(amount, registers[condition_reg], condition, compare_val, "yes" if res else "no"))
    if res:
        registers[update_reg] += amount
        highest_val = max(highest_val, registers[update_reg]) 
    print(registers)

highest_reg = max(registers.iterkeys(), key=(lambda key: registers[key]))
print("Highest register at end is %s at %d"%(highest_reg, registers[highest_reg]))
print("Highest register value at any time was %d"%(highest_val))

