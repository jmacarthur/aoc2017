#!/usr/bin/python

import sys
sys.path.insert(0, '../day10')
from solve10b import knot_hash

real_input = "jxqlasbh"
test_input = "flqrgnkx"
hash_base = real_input

used_spaces = 0
disc = []

def find_occupied_space(disc):
    for y in range(0,128):
        row = disc[y]
        for x in range(0,128):
            if row[x] == '#': return (x,y)
    return None

def delete_region((x,y)):
    disc[y][x] = '.'
    neighbours = [ (x+1, y), (x-1, y), (x, y+1), (x, y-1) ]
    for (nx,ny) in neighbours:
        if nx >=0 and ny >= 0 and nx < 128 and ny < 128:
            if disc[ny][nx] == '#': delete_region((nx, ny))

for row in range(0,128):
    line_input = "%s-%d"%(hash_base, row)
    hash_list = knot_hash(line_input)
    line_int = 0
    line = []
    for i in range(0,16):
        line.extend(['.' if (hash_list[i] & (1<<bit)) == 0 else '#' for bit in range(7,-1,-1)])
    used_spaces += line.count('#')
    print("%s %16.16s"%(line_input, "".join(line)))
    disc.append(line)

regions = 0
while True:
    pos = find_occupied_space(disc)
    if pos == None: break
    print("Deleting region at %d, %d"%pos)
    regions += 1
    delete_region(pos)

print ("%d used spaces"%used_spaces)
print ("%d regions"%regions)
