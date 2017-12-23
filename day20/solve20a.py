#!/usr/bin/python

import sys

with open(sys.argv[1], 'rt') as f:
    particles = []
    while True:
        l = f.readline()
        if l == "": break
        fields = l.split(", ")
        stripped_fields = [field.lstrip("pva=<").rstrip(">\n") for field in fields]
        particles.append([map(int,field.split(",")) for field in stripped_fields])

print particles

# Distance is manhattan distance (abs(x)+abs(y)+abs(z))
# The position after n cycles is the n* square of the acceleration, plus n* velocity, plus position
cycle = 1000000000000
closest = None
for p in range(0,len(particles)):
    particles[p][1] = [x+y*cycle for x,y in zip(particles[p][1], particles[p][2])]
    particles[p][0] = [x+y*cycle for x,y in zip(particles[p][0], particles[p][1])]
    dist = sum(map(abs, particles[p][0]))
    if closest == None or dist < closest:
        closest = dist
        closest_num = p

print("Closest particle on cycle %d is %d at %d blocks away"%(cycle, closest_num, closest))
