#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

DOPART1 = True
DOPART2 = True
DEBUG = True

with open('day10.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()]   # 

testdata2 = [x.strip() for x in """...0...
...1...
...2...
6543456
7.....7
8.....8
9.....9
""".splitlines()]

testdata3 = [x.strip() for x in """..90..9
...1.98
...2..7
6543456
765.987
876....
987....""".splitlines()]


thedata = testdata
thedata = alldata



DIRS4 = [  (0,-1),(1,0),(0,1),(-1,0)]  # north, east, south, west, rotatable (idir+1)%4
DIRS4NAME = ['n','e','s','w']

WIDTH = len(thedata[0])
HEIGHT = len(thedata)

def isInBounds(ix:int, iy:int) -> bool:
    if (ix>=0) and (ix < WIDTH) and (iy>=0) and (iy < HEIGHT):
        return True
    return False
# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

class Node:
    def __init__(self, loc=None, parent=None):
        self.parent = parent
        self.loc = loc  # tuple(x,y) position
        self.children = []  # list of potential Nodes

    def findPotentialChildren(self, thislevel:int) -> int:
        self.children = []
        nextlevel = thislevel + 1
        for adir in DIRS4:
            ix = self.loc[0] + adir[0]
            iy = self.loc[1] + adir[1]
            if isInBounds(ix,iy):
                if thedata[iy][ix] == str(nextlevel):
                    anode = Node( (ix,iy), self)
                    if nextlevel <=8:
                        subchildren = anode.findPotentialChildren(nextlevel)
                        if subchildren > 0:
                            self.children.append(anode)
                    else:
                        # no need to go further if found level 9's
                        self.children.append(anode)

        return len(self.children)
    
    def countLeafs(self) -> int:
        if len(self.children) == 0:
            return 1
        # otherwise, add up from below
        leafs = 0
        for achild in self.children:
            leafs += achild.countLeafs()
        return leafs
    
    def reachedLeafPositions(self, positions:dict):
        if len(self.children) == 0:
            positions[self.loc] = positions.get(self.loc, 0) + 1
            return
        # otherwise, try below
        for achild in self.children:
            achild.reachedLeafPositions(positions)

if DOPART1:

    START = time.perf_counter()

    trails = []
    for iy in range(HEIGHT):
        for ix in range(WIDTH):
            if thedata[iy][ix] == '0':
                # this is trailhead
                trailheadnode = Node( (ix,iy), None)
                trails.append(trailheadnode)
                trailheadnode.findPotentialChildren(0)

    sum = 0
    for atrailhead in trails:
        positions = {}
        atrailhead.reachedLeafPositions(positions)
        thistrailcount = len(positions)
        if DEBUG:
            print(f"Trailhead at {atrailhead.loc} as {thistrailcount} unique endpoints")
        sum += thistrailcount

    print(f"Part 1: total score = {sum}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    if not DOPART1:
        print("Hey, do part 1!")


    sum = 0
    for atrailhead in trails:
        thistrailcount = atrailhead.countLeafs()
        if DEBUG:
            print(f"Trailhead at {atrailhead.loc} as {thistrailcount} paths")
        sum += thistrailcount

    print(f"Part 2: total rating = {sum}")

    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")