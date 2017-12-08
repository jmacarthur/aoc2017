#!/usr/bin/python -w

f = open("input5.txt")

indexes = map(int, f.readlines())


pos = 0
steps = 0
while True:
    if(pos >=  len(indexes) or pos < 0):
        print("Escaped list to index %d"%pos)
        break
    steps += 1
    offset = indexes[pos]
    if(offset >= 3):
        indexes[pos] -= 1
    else:
        indexes[pos] += 1
    pos += offset
    print("Jumped by %d to index %d"%(offset, pos))

print("Executed %d steps"%steps)
