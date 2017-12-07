#!/usr/bin/python -w

import copy

f = open("input5.txt", "rt")
banks = map(int,f.readline().strip().split())
history = []
cycle_log = []

print banks
cycles = 0

while True:
    highest_value = max(banks)
    # Find the highest bank - there can be several indexes equal to
    # highest_value, but we want the first one in every case
    highest_bank = banks.index(highest_value)
    banks[highest_bank] = 0
    cycles += 1
    distributing_bank = highest_bank
    for i in range(0,highest_value):
        distributing_bank += 1
        distributing_bank %= len(banks)
        banks[distributing_bank] += 1

    if banks in history:
        old_index = history.index(banks)+1
        print "Duplicated entry:"
        print banks
        print "Previous version appeared at %d (%d loop size)"%(old_index, cycles-old_index)
        print "Processed %d cycles"%cycles
        break
    else:
        history.append(copy.copy(banks))
        print banks
