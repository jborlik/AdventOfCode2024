import itertools
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

with open('day08.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()]   # 


thedata = testdata
thedata = alldata

HEIGHT = len(thedata)
WIDTH = len(thedata[0])

def processInput(adata) -> dict:
    # dict[ Freq:str ] = [ list of (ix,iy) ]
    freqs = {}
    for iy in range(HEIGHT):
        for ix in range(WIDTH):
            achar = adata[iy][ix]
            if achar != '.':
                lst = freqs.get(achar, [])
                lst.append( (ix,iy) )
                freqs[achar] = lst
    return freqs

freqs = processInput(thedata)

if DEBUG:
    print(freqs)

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def findNodes(afreq, listLocs, infiniteNodes: bool):
    listNodes = []
    for combo in itertools.combinations(listLocs, r=2):
        ixdiff = combo[1][0] - combo[0][0]
        iydiff = combo[1][1] - combo[0][1]
        MAXNODES = 10000 if infiniteNodes else 1
        # positive direction
        for i in range(0,MAXNODES+1):
            potnode = (combo[1][0] + i*ixdiff, combo[1][1] + i*iydiff)
            if potnode[0] < 0 or potnode[0] >= WIDTH or potnode[1] < 0 or potnode[1] >= HEIGHT:
                break
            listNodes.append(potnode)
        # negative direction
        for i in range(0,MAXNODES+1):
            potnode = (combo[0][0] - i*ixdiff, combo[0][1] - i*iydiff)
            if potnode[0] < 0 or potnode[0] >= WIDTH or potnode[1] < 0 or potnode[1] >= HEIGHT:
                break
            listNodes.append(potnode)        


    return listNodes        
        

if DOPART1:

    START = time.perf_counter()

    locs = {}
    for afreq, listLocs in freqs.items():
        listNodes = findNodes(afreq,listLocs,infiniteNodes=False)
        for anode in listNodes:
            locs[anode] = locs.get(anode, 0) + 1
    
    print(f"Part 1: unique locs = {len(locs)}")



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    locs = {}
    for afreq, listLocs in freqs.items():
        listNodes = findNodes(afreq,listLocs,infiniteNodes=True)
        for anode in listNodes:
            locs[anode] = locs.get(anode, 0) + 1
    
    print(f"Part 2: unique locs = {len(locs)}")




    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")