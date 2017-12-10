#!/usr/bin/python

import sys

def swap_list_elements(l, a, b):
    wrap = len(l)
    print("Swap %d and %d (wrapped to %d and %d)"%(a,b, a%wrap,b%wrap))
    (l[a % wrap], l[b % wrap]) = (l[b % wrap], l[a % wrap])

def reverse_in_place(ring, l, pos):
    for x in range(0,l/2):
        y = l-x-1
        swap_list_elements(ring, pos+x, pos+y)

def process_reversions(lengths):
    ring = range(0,256)
    pos = 0
    skip = 0
    print ring
    for l in lengths:
        print("Reversing: length %d from pos %d with skip %d"%(l, pos, skip))
        reverse_in_place(ring, l, pos)
        pos += l
        pos += skip
        skip += 1
        pos = pos % len(ring)
        print ring

def main():
    filename = sys.argv[1]
    with open(filename, "rt") as f:
        lengths = f.readlines()
    for l in lengths:
       print("Processing line")
       process_reversions(map(int, l.strip().split(',')))
       print("----------------------------------------")

if __name__=="__main__":
    main()
