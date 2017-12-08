#!/usr/bin/env python

import sys

target = int(sys.argv[1])

n = 1
x = 0
y = 0

UP = 0
LEFT = 1
DOWN = 2
RIGHT = 3

radius = 1;
directions = ['up', 'left', 'down', 'right']
deltas = [(0,1), (-1,0), (0,-1), (1,0)]

field = [None]*1024
for i in range(0,1024):
    field[i] = [None]*1024

field[512][512] = 1
    
def abs(x):
    return -x if x<0 else x

def update_field(x,y):
    global field
    total = 0
    for dx in range(-1,2):
        for dy in range(-1,2):
            f = field[x+dx+512][y+dy+512]
            if f is not None:
                total += f
    field[x+512][y+512] = total
    print("Found total %d at %d, %d"%(total,x,y))
    if total > target:
        print("Found total %d at %d, %d"%(total,x,y))

        for py in range(4,-5,-1):
            for px in range(-4,5):
                if field[px+512][py+512] is None:
                    sys.stdout.write("---\t")
                else:
                    sys.stdout.write("%d\t"%(field[px+512][py+512]))
            print("\n")
        sys.exit(1)

def traverse(a, direction):
    global n,x,y
    print("Traverse %d %s"%(a, directions[direction]))
    for i in range(0,a):
        n += 1
        x += deltas[direction][0]
        y += deltas[direction][1]
        print("%d at %d,%d =dist %d"%(n,x,y,abs(x)+abs(y)))
        update_field(x,y)

traverse(1,RIGHT)
        
while True:
    traverse(radius, UP)
    traverse(2*radius, LEFT)
    traverse(2*radius, DOWN)
    traverse(2*radius+1, RIGHT)
    traverse(radius, UP)
    radius += 1
