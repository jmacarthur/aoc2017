#!/bin/bash
grep -- "->" input7.txt > trees
cut -d' ' -f1 trees > supporters
cut -d'>' -f2 trees > supportees
for i in `cat supporters`; do grep $i supportees || echo "$i is the base"; done | grep base

