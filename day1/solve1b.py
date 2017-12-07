#!/usr/bin/env python

f = open("input1.txt", "rt")
l = f.readline().strip()

sum = 0

size = len(l)
print("%d elements" % size)
delta = size/2
for x in range(0,size):
    val = int(l[x])
    if(val>0):
        if l[x] == l[(x+delta)%size]:
            sum += val
print sum

    
    
