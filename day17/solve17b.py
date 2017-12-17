#!/usr/bin/python

test_input = 3
real_input = 386
step = real_input

buffer = [0]
pos = 0
l = 1
while l < 50000001:
    pos = (pos + step) % l
    if(pos==0): print("Inserting after 0: %d"%l)
    l += 1
    pos = (pos + 1) % l

