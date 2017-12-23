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

cycle = 0

while cycle < 10000000:
    particle_pos = []
    for p in range(0,len(particles)):
        if particles[p] is None: continue
        particles[p][1] = [x+y for x,y in zip(particles[p][1], particles[p][2])]
        particles[p][0] = [x+y for x,y in zip(particles[p][0], particles[p][1])]
        particle_pos.append((p, particles[p][0]))

    # Sort all the particles by their Manhattan distance from (0,0,0) - if two
    # particles collide, they must have the same Manhattan distance.
    sorted_particle_pos = sorted(particle_pos, key=lambda x: sum(map(abs, x[1])))
    for p in range(0,len(sorted_particle_pos)-1):
        if sorted_particle_pos[p][1] == sorted_particle_pos[p+1][1]:
            print("Particles %d and %d collide at %r"%(sorted_particle_pos[p][0], sorted_particle_pos[p+1][0], sorted_particle_pos[p][1]))
            particles[sorted_particle_pos[p][0]] = None
            particles[sorted_particle_pos[p+1][0]] = None
    cycle += 1
    if(cycle % 1000 == 0):
        print("Cycle %d: %d particles remaining"%(cycle, len(sorted_particle_pos)))
