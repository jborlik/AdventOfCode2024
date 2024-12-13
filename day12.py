#import itertools
#import numpy as np
import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

DOPART1 = True
DOPART2 = True
DEBUG = True

with open('day12.txt') as datafile:
    alldata = [list(x.strip()) for x in datafile.readlines()]

testdata = [list(x.strip()) for x in """AAAA
BBCD
BBCC
EEEC""".splitlines()]   # 

testdata2 = [list(x.strip()) for x in """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO""".splitlines()]   # 

testdata3 = [list(x.strip()) for x in """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE""".splitlines()]   # 

thedata = testdata3
thedata = alldata

WIDTH = len(thedata[0])
HEIGHT = len(thedata)

DIRS4 = [  (0,-1),(1,0),(0,1),(-1,0)]  # north, east, south, west, rotatable (idir+1)%4
DIRS4NAME = ['n','e','s','w']

class Field:
    def __init__(self, atype:str):
        self.type = atype  # char
        self.bordercount = 0  # known border length
        self.tiles = []  # list of ix,iy tuples   area=len(tiles)

    def calcprice(self) -> int:
        return len(self.tiles) * self.bordercount
    
    def __repr__(self):
        return f"[{self.type}: area={len(self.tiles)} border={self.bordercount} tiles={self.tiles}]\n"

PROCESSED = '.'

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------
def isInBounds(ix:int, iy:int) -> bool:
    if (ix>=0) and (ix < WIDTH) and (iy>=0) and (iy < HEIGHT):
        return True
    return False

def replaceAt(allfields, ix, iy, achar):
    #allfields[iy] = allfields[iy][:ix] + achar + allfields[iy][ix+1:]
    allfields[iy][ix] = achar

def checkSquare(allfields, afield, ix, iy) -> bool:
    if not isInBounds(ix,iy):
        return False
    
    atype = allfields[iy][ix]
    if atype==afield.type:
        # yes, this is one
        afield.tiles.append( (ix,iy) )
        replaceAt(allfields, ix, iy, str.lower(atype))  # first pass lcase (which will prevent adds), after done 
        # try neighbors
        for adir in DIRS4:
            ixn, iyn = ix+adir[0], iy+adir[1]
            gotone = checkSquare(allfields, afield, ixn, iyn)
            if not gotone:
                # was it not added because it was already added?
                if isInBounds(ixn, iyn) and allfields[iyn][ixn] == str.lower(atype):
                    pass
                else:
                    afield.bordercount += 1

        return True
    else:
        # nope
        return False
    
if DOPART1:

    START = time.perf_counter()

    allfields = copy.deepcopy(thedata)   # we will rewrite some of this
    fields = []

    for iy in range(WIDTH):
        for ix in range(HEIGHT):
            atype = allfields[iy][ix]
            if atype == PROCESSED:
                continue
            # this is a new field
            afield = Field(atype)
            checkSquare(allfields, afield, ix, iy)  # this will allocate it and recursively find all
            # mark all as processed
            for achild in afield.tiles:
                replaceAt(allfields, achild[0], achild[1], PROCESSED)

            fields.append(afield)

    print(fields)

    price = sum([s.calcprice() for s in fields])
    print(f"Part 1:  total price = {price}")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()




    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")