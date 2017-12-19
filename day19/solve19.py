#!/usr/bin/python

import sys
import logging

logging.basicConfig(level=logging.WARNING)

EAST = 0
NORTH = 1
WEST = 2
SOUTH = 3

dx = [ 1, 0, -1, 0 ]
dy = [ 0, -1, 0, 1 ]

def read_map(filename):
    with open(filename, "rt") as f:
        m = [x.strip('\n') for x in f.readlines()]
    return m

def find_start(m):
    """ We always start on row 0, and there should be exactly one vertical bar in that row """
    print("Initial row is: "+m[0])
    y = 0
    x = m[y].index("|")
    return (x,y)

def get_map(m, tx, ty):
    if ty>=len(m) or ty<0 or tx>=len(m[ty]) or tx<0:
        return "^"
    return m[ty][tx]

def get_ahead(m, x, y, d):
    (tx,ty) = (x + dx[d], y+dy[d])
    return get_map(m, tx, ty)

def get_left(m, x, y, d):
    d = (d+1)%4
    (tx,ty) = (x + dx[d], y+dy[d])
    return get_map(m, tx, ty)

def get_right(m, x, y, d):
    d = (d+3)%4
    (tx,ty) = (x + dx[d], y+dy[d])
    return get_map(m, tx, ty)

def run_step(m, x, y, d, steps):
    ahead = get_ahead(m, x, y, d)
    
    disallowed_set = [' ', '^']
    if ahead in disallowed_set: # Can't go forward
        if get_left(m, x, y, d) not in disallowed_set:
            d = (d+1)%4 # Turn left
            logging.debug("Turning left at %d,%d to direction %d"%(x,y,d))

        elif get_right(m, x, y, d) not in disallowed_set:
            d = (d+3)%4 # Turn right
            logging.debug("Turning right at %d,%d to direction %d"%(x,y,d))
        else:
            print("Can't go straight on, left or right at %d,%d - aborting after %d steps"%(x,y, steps))
            sys.exit(1)
    else:
        # Can go forward
        if ahead.isalpha():
            print("Crossed letter %c"%ahead)
        else:
            logging.debug("Passing symbol %c at (%d,%d)"%(ahead,x,y))
        x = x+dx[d]
        y = y+dy[d]
        steps += 1
    return (x,y,d, steps)

def run_map(m):
    (x,y) = find_start(m)
    logging.debug("Starting at (%d,%d)"%(x,y))
    d = SOUTH
    steps = 1 # Includes the one it started on
    while True:
        (x,y,d, steps) = run_step(m, x,y,d, steps)

def main():
    m = read_map(sys.argv[1])
    run_map(m)

main()
