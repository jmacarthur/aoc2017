#!/usr/bin/python

import copy
import sys
import logging
logging.basicConfig(level=logging.INFO)

transform_cache_2 = {}
transform_cache_3 = {}

class Sprite(object):
    def __init__(self, size):
        self.size = size
        self.pixels = []
        for y in range(0,size):
            self.pixels.append([0]*size)
    def integer_val(self,ox,oy,size):
        bit = 0
        val = 0
        for x in range(0,size):
            for y in range(0,size):
               val |= (self.pixels[oy+y][ox+x] << bit)
               bit += 1
        return val
    @staticmethod
    def pixelarray(size):
        pixels = []
        for y in range(0,size):
            pixels.append([0]*size)
        return pixels
    @staticmethod
    def convert_line(line):
        return [1 if x=='#' else 0 for x in line]
    @staticmethod
    def from_text(text):
        rows = text.split("/")
        size = len(rows)
        n = Sprite(size)
        n.pixels = [Sprite.convert_line(x) for x in rows]
        return n
    def duplicate(self):
        n = Sprite(self.size)
        n.pixels = copy.deepcopy(self.pixels)
        return n
    def direct_match_flip_v(self, pattern, x, y, size):
        for py in range(0,size):
            if self.pixels[y+py][x:x+size] != pattern.pixels[size-1-py]:
                return False
        logging.debug("Match!")
        return True
    def direct_match_flip_h(self, pattern, x, y, size):
        for px in range(0,size):
            for py in range(0,size):
                if self.pixels[y+py][x+px] != pattern.pixels[py][size-1-px]:
                    return False
        logging.debug("Match!")
        return True
    def direct_match(self, pattern, x, y, size):
        for py in range(0,size):
            if self.pixels[y+py][x:x+size] != pattern.pixels[py]:
                return False
        logging.debug("Match!")
        return True
    def rotate_ccw(self):
        n = Sprite.pixelarray(self.size)
        for row in range(0,self.size):
            for col in range(0,self.size):
                n[self.size-1-col][row] = self.pixels[row][col]
        self.pixels = n
    def match(self, x, y, size, pattern):
        logging.debug("Looking for %r at %d,%d",pattern,x,y)
        if pattern.size != size: return False
        p = pattern.duplicate()
        for d in range(0,4):
            if self.direct_match(p, x, y, size) or self.direct_match_flip_v(p,x,y,size) or self.direct_match_flip_h(p,x,y,size):
                return True
            p.rotate_ccw()
            # If rotating has no effect, don't continue
            if p.direct_match(pattern,0,0,p.size):
                return False
        return False
    def blit(self, source, x, y):
        for px in range(source.size):
            for py in range(source.size):
                self.pixels[y+py][x+px] = source.pixels[py][px]
    @staticmethod
    def _transline(r):
        return "".join(['#' if c == 1 else '.' for c in r])
    def __repr__(self):
        return "/".join([Sprite._transline(r) for r in self.pixels])
    def count_pixels(self):
        count = 0
        for x in range(0,self.size):
            for y in range(0,self.size):
                count += self.pixels[y][x]
        return count
    def verbose_print(self):
        def transline(r):
            return "".join(['#' if c == 1 else '.' for c in r])
        return "\n".join([Sprite._transline(r) for r in self.pixels])

def apply_transforms(sprite, x, y, size, transforms,destination):
    """Try to apply each of the transforms in order until one fits. x and
    y are cell coordinates and must be multiplied by the cell size to get
    pixels."""
    origin_int = sprite.integer_val(x*size, y*size, size)
    if size==2 and origin_int in transform_cache_2:
        destination.blit(transform_cache_2[origin_int], x*(size+1), y*(size+1))
        return True
    elif size==3 and origin_int in transform_cache_3:
        destination.blit(transform_cache_3[origin_int], x*(size+1), y*(size+1))
        return True

    for (start,finish) in transforms:
        if sprite.match(x*size,y*size,size,start):
            if size == 2:
                transform_cache_2[origin_int] = finish
            elif size == 3:
                transform_cache_3[origin_int] = finish
            logging.debug("Original: %r",destination)
            logging.debug("Blitting %r at %d, %d",finish,x,y)
            destination.blit(finish, x*(size+1), y*(size+1))
            logging.debug("Result: %r",destination)
            return True
    return False

def iterate(sprite, transforms_2, transforms_3):
    if sprite.size % 2 == 0:
        cells = sprite.size / 2
        destination = Sprite(cells*3)
        for x in range(0,cells):
            for y in range(0,cells):
                if not apply_transforms(sprite, x, y, 2, transforms_2, destination):
                    logging.error("No pattern matched at cell %d, %d",x,y)
                    sys.exit(1)
    elif sprite.size % 3 == 0:
        cells = sprite.size / 3
        destination = Sprite(cells*4)
        for x in range(0,cells):
            for y in range(0,cells):
                if not apply_transforms(sprite, x, y, 3, transforms_3, destination):
                    logging.error("No pattern matched at cell %d, %d",x,y)
                    sys.exit(1)
    else:
        logging.error("Illegal sprite size %d"%sprite.size)
        sys.exit(2)
    return destination

def main():
    with open(sys.argv[1], "rt") as f:
        lines = [x.strip() for x in f.readlines()]
    transforms_2 = []
    transforms_3 = []
    for l in lines:
        (start, finish) = l.split(" => ")
        s = Sprite.from_text(start)
        f = Sprite.from_text(finish)
        if s.size==2:
            transforms_2.append((s,f))
        elif s.size==3:
            transforms_3.append((s,f))

    s = Sprite(3)
    s.pixels = [[0,1,0], [0,0,1], [1,1,1]]
    for i in range(0,18):
        logging.info("----- Iteration %d; size %d"%(i, s.size))
        s = iterate(s, transforms_2, transforms_3)
        logging.info("New pattern has %d pixels"%s.count_pixels())

if __name__=="__main__": main()
