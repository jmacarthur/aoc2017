#!/usr/bin/python

import sys

network = []
reachable_nodes = []

with open(sys.argv[1]) as f:
    for l in f.readlines():
        fields = l.strip().split(" <-> ")
        connections = fields[1].split(", ")
        network.append(map(int, connections))

explored_nodes = {}

def explore(starting_point):
    global explored_nodes
    to_explore = [starting_point]

    while len(to_explore) > 0:
        node = to_explore.pop()
        explored_nodes[node] = True
        for n in network[node]:
            if n not in explored_nodes:
                to_explore.append(n)

explore(0)
print("%d nodes reachable from 0: %r"%(len(explored_nodes), explored_nodes.keys()))

separate_groups = 1
for pos in range(1,len(network)):
    if pos not in explored_nodes:
        separate_groups += 1
        explore(pos)

print("%d separate groups exist."%separate_groups)
