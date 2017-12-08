#!/usr/bin/python

f = open("input4.txt","rt")

valid = 0
rejected = 0

while True:
    l = f.readline().strip()
    words = set()
    if l == "": break
    for w in l.split():
        sortedletters = "".join(sorted(w))
        if sortedletters in words:
            print("Rejected %s - %s already present"%(l,w))
            rejected += 1
            break
        else:
            words.add(sortedletters)
    else:
        valid += 1

print("%d valid words and %d rejected words"%(valid,rejected))
