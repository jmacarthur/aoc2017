#!/usr/bin/python

test_input = 3
real_input = 386
step = real_input

buffer = [0]
pos = 0

for n in range(1,2018):
    pos = (pos + step) % len(buffer)
    buffer.insert(pos+1,n)
    pos = (pos + 1) % len(buffer)
    print buffer
    print pos

