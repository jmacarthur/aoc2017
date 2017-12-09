#!/usr/bin/env python

import sys

def parse_line(l):
    print("Processing line %s"%l.strip())
    input_data = list(l.strip())

    mode = "Group" # Either "Group" or "Garbage"
    group_level = 0 # The current group nesting level
    group_levels = [] # Array showing the level of each group when we start it
    garbage_count = 0 # Amount of garbage counted so far, not counting cancelled characters
    pos = 0 # Position in string that's currently being processed - only required for debugging

    while len(input_data)>0:
        c = input_data.pop(0)
        pos += 1
        print("Processing '%c' in mode %s"%(c,mode_string[mode]))
        if mode == "Group":
            if c == '}':
                group_level -= 1
                if(group_level < 0):
                    print("} without matching { at pos %d" % pos);
                    sys.exit(1)
            elif c == '{':
                group_level += 1
                group_levels.append(group_level)
            elif c == '<':
                mode = "Garbage"
        elif mode == "Garbage":
            if c == '!':
                input_data.pop(0)
                pos += 1
            elif c == '>':
                mode = "Group"
            else:
                garbage_count += 1

    print("-------------------- Group levels: %r = %s; garbage count = %d"%(group_levels,sum(group_levels), garbage_count))

if __name__ == "__main__":
    input_file = open(sys.argv[1], "rt")
    for l in input_file.readlines():
        parse_line(l)

