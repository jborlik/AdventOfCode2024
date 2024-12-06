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

with open('day06.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()]   # 


thedata = testdata
thedata = alldata

DIRS4 = [  (0,-1),(1,0),(0,1),(-1,0)]  # north, east, south, west.
DIRS4NAME = ['n','e','s','w']
DIRS4CHAR = ['^','>','v','<']

WALL = -1

def processMap(stringdata) -> tuple[dict, tuple, int]:
    """Parses map, making dict[ (ix,iy) ]=(count or -1 for walls), (iguardx,iguardy), iguarddir"""
    mapdict = {}
    iguardloc = ()
    iguarddir = 0
    for ix in range(len(stringdata[0])):
        for iy in range(len(stringdata)):
            achar = stringdata[iy][ix]
            if achar == "#":
                mapdict[ (ix,iy) ] = WALL  # a 
            elif achar in DIRS4CHAR:
                iguarddir = DIRS4CHAR.index(achar)
                iguardloc = (ix,iy)
    return mapdict, iguardloc,iguarddir

walls, guardloc, guarddir = processMap(thedata)
print(f"Starting guardloc={guardloc} dir={guarddir}")
width = len(thedata[0])
height = len(thedata)


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def walkMap(awalls, aguardloc, aguarddir) -> tuple[dict, bool]:
    """ returns visitdict and True if exited"""
    visitdict = {}

    while (aguardloc[0] >=0) and (aguardloc[1] >= 0) and (aguardloc[0] < width) and (aguardloc[1] < height):
        # was I here below, and was I going in the same direction?
        if aguardloc in visitdict:
            olddir = visitdict[aguardloc]
            if olddir == aguarddir:
                # you are looping, boy
                return visitdict, False
            
        visitdict[ aguardloc ] = aguarddir

        # take a step in the dir
        # can I move forward in same direction?
        newloc = (aguardloc[0] + DIRS4[aguarddir][0],  aguardloc[1] + DIRS4[aguarddir][1])
        while newloc in awalls:
            # change dir
            aguarddir = (aguarddir + 1) % 4
            newloc = (aguardloc[0] + DIRS4[aguarddir][0],  aguardloc[1] + DIRS4[aguarddir][1])

        # step taken
        aguardloc = newloc
    
    # supposedly I just exit
    return visitdict, True



if DOPART1:

    START = time.perf_counter()

    visitdict = {}

    visitdict, isexited = walkMap(walls, guardloc, guarddir)

    # supposedly I just exit
    if DEBUG:
        print(f"Part 1: exited? {isexited}")
        print(f" Guard loc = {guardloc}")
    sum = len(visitdict)
    print(f"Part 1:  visited {sum} squares")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    # try each open space and see if adding a wall makes a difference

    loops = 0

    for ix in range(len(thedata[0])):
        for iy in range(len(thedata)):

            if (ix,iy) not in walls:
                if (ix != guardloc[0]) or (iy != guardloc[1]):
                    # let's try adding one
                    newwalls = copy.deepcopy(walls)
                    newwalls[ (ix,iy) ] = WALL

                    visitdict, isexited = walkMap(newwalls, guardloc, guarddir)
                    if not isexited:
                        loops = loops + 1
                        if DEBUG:
                            print(f"Loop if adding obs at {ix},{iy}")

    print(f"Part 2: loop options = {loops}")



    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")