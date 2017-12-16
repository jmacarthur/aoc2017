#!/usr/bin/python

import sys
import operator # For xor
def swap_list_elements(l, a, b):
    wrap = len(l)
    (l[a % wrap], l[b % wrap]) = (l[b % wrap], l[a % wrap])

def reverse_in_place(ring, l, pos):
    for x in range(0,l/2):
        y = l-x-1
        swap_list_elements(ring, pos+x, pos+y)

def xor_16_byte(array):
    output = []
    for i in range(0, len(array), 16):
        output.append(reduce(operator.xor, array[i:i+16]))
    return output

def process_reversions(lengths):
    ring = range(0,256)
    pos = 0
    skip = 0
    for r in range(0,64):
        for l in lengths:
            reverse_in_place(ring, l, pos)
            pos += l
            pos += skip
            skip += 1
            pos = pos % len(ring)
    print ring
    hashval = xor_16_byte(ring)
    return hashval

def knot_hash(inp):
    reversions = map(ord, inp)
    reversions.extend([17, 31, 73, 47, 23])
    hashval = process_reversions(reversions)
    return hashval

def main():
    filename = sys.argv[1]
    with open(filename, "rt") as f:
        lengths = f.readlines()
    for l in lengths:
       print("Processing line '%s'"%l.strip())
       hashval = knot_hash(l.strip())
       hashascii = "".join(["%2.2x"%x for x in hashval])
       print hashascii
       print("----------------------------------------")

if __name__=="__main__":
    main()
