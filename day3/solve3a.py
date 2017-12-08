#!/usr/bin/env python

import sys

target = int(sys.argv[1])

n = 2
x = 1
y = 0

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

radius = 1;
directions = ['up', 'left', 'down', 'right']
deltas = [(0,1), (-1,0), (0,-1), (1,0)]

def abs(x):
    return -x if x<0 else x

def traverse(a, direction):
    global n,x,y
    print("Traverse %d %s"%(a, directions[direction]))
    for i in range(0,a):
        n += 1
        x += deltas[direction][0]
        y += deltas[direction][1]
        print("%d at %d,%d =dist %d"%(n,x,y,abs(x)+abs(y)))

while n < target:
    traverse(radius, UP)
    traverse(2*radius, LEFT)
    traverse(2*radius, DOWN)
    traverse(2*radius+1, RIGHT)
    traverse(radius, UP)
    radius += 1
