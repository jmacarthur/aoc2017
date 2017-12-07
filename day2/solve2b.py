#!/usr/bin/env python
f = open("input2.txt","rt")
lines = []
while True:
    l = f.readline().strip()
    if l == "": break
    lines.append(map(int,l.split()))

total = 0
for l in lines:
    for n in l:
        for d in l:
            if n % d==0 and n!=d:
                print("%d / %d = %d"%(n, d, n/d))
                total += n/d

print total
