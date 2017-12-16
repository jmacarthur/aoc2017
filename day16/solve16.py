#!/usr/bin/python

import sys
import copy
stage_length = 16
stage = map(chr, range(ord('a'),ord('a')+stage_length))

def spin(amount):
    """To save time, this function isn't used except at the end.
    Normally, a counter marks the start of the stage and this changes
    instead. """
    global stage
    stage = stage[amount:] + stage[:amount]

def swap(pos1, pos2):
    global stage
    (stage[pos1], stage[pos2]) = (stage[pos2], stage[pos1])

with open(sys.argv[1], 'rt') as f:
    program = ",".join(f.readlines()).split(",")

n = 0
pos = 0
arguments_list = [x[1:].strip().split("/") for x in program]
action_list = [x[0] for x in program]
history = []

# Change this to 1 for the solution to part 1.
iterations = 1000000000

while n<iterations:
    for s in range(0,len(program)):
        arguments = arguments_list[s]
        if action_list[s] == 's':
            pos += stage_length-int(arguments[0])
        elif action_list[s] == 'x':
            swap((int(arguments[0])+pos)%stage_length, (int(arguments[1])+pos)%stage_length)
        elif action_list[s] == 'p':
            pos1 = stage.index(arguments[0])
            pos2 = stage.index(arguments[1])
            swap(pos1, pos2)
    if stage in history:
        print("Duplicate found: %r at index %d matches at stage %d"%(stage, history.index(stage), n))
        loop_length = n - history.index(stage)
        complete_cycles = (iterations - n) / loop_length
        n += complete_cycles * loop_length
    history.append(copy.copy(stage))
    n += 1

spin(pos % stage_length)
print "".join(stage)
