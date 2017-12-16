#!/usr/bin/python

test_input = (65,8921)
real_input = (703, 516)
(a,b) = real_input

limit = 2147483647
matches = 0
iterations = 40000000
n = 0
while n < iterations:
    a = a*16807 % limit
    b = b*48271 % limit
    if a & 0xFFFF == b & 0xFFFF:
        matches += 1
        print("Match at %d"%n)
    n += 1
print matches
