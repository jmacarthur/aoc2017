#!/usr/bin/python

import sys
import copy
with open(sys.argv[1], 'rt') as f:
    lines = [l.strip() for l in f.readlines()]
    ports = [map(int, l.split('/')) for l in lines]

used_ports = []

longest = 0
highscore = 0

def record_highscore(used_ports):
    global highscore, longest
    power = sum([x+y for (x,y) in used_ports])
    length = len(used_ports)
    if(length >= longest):
        if(length > longest): highscore = 0
        longest = length
        if(power > highscore):
            highscore = power
            print("Chain found: power %d len %d, %r."%(power,length, used_ports))

def find_chain(used_ports, current_port):
    found_chain = False
    for i in ports:
        if i in used_ports: continue
        if i[0]==current_port or i[1]==current_port:
            new_ports = copy.deepcopy(used_ports)
            new_ports.append(i)
            if i[0]==current_port:
                find_chain(new_ports, i[1])
            else:
                find_chain(new_ports, i[0])
            found_chain = True
    if not found_chain:
        record_highscore(used_ports)

find_chain([], 0)
    
