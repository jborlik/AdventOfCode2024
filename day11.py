#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

DOPART1 = False
DOPART2 = True
DEBUG = False

with open('day11.txt') as datafile:
    alldata = datafile.readline().strip().split(' ')

testdata = "0 1 10 99 999".split(' ')
testdata2 = "125 17".split(' ')

STEPS1 = 25
STEPS2 = 75

thedata = testdata2
thedata = alldata


def processStep( oldstones: list) -> list:
    newstones = []
    for oldstone in oldstones:
        if oldstone == '0':
            newstones.append('1')
        elif len(oldstone) % 2 == 0:
            mid = len(oldstone) // 2
            newstones.append(str(int(oldstone[:mid])))
            newstones.append(str(int(oldstone[mid:])))
        else:
            newstones.append( str(int(oldstone) * 2024) )
    return newstones

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if DOPART1:

    START = time.perf_counter()

    if DEBUG:
        print(f"Initial: {thedata}")
    oldstones = thedata

    for istep in range(STEPS1):
        oldstones = processStep(oldstones)
        if DEBUG:
            print(f"Step {istep}: {oldstones}")
        else:
            print(f"Step {istep}: {len(oldstones)}")
        

    print(f"Part1: End with {len(oldstones)} stones")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

def blinkDict(oldstones: dict) -> dict:
    newstones = {}
    for s in oldstones:
        if s == '0':
            newstones['1'] = newstones.get('1', 0) + oldstones[s]
        elif len(s) % 2 == 0:
            mid = len(s) // 2
            sleft = str(int(s[:mid]))
            sright = str(int(s[mid:]))
            newstones[sleft] = newstones.get(sleft, 0) + oldstones[s]
            newstones[sright] = newstones.get(sright, 0) + oldstones[s]
        else:
            s2024 = str(int(s) * 2024)
            newstones[s2024] = newstones.get(s2024, 0) + oldstones[s]
    return newstones



if DOPART2:
    START = time.perf_counter()

    oldstones = {}
    for i in thedata:
        oldstones[i] = oldstones.get(i,0) + 1

    for iblink in range(STEPS2):
        oldstones = blinkDict(oldstones)
        if DEBUG:
            print(f"  {iblink} steps: {oldstones}")

    print(f"Part 2: Final count = {sum(oldstones[s] for s in oldstones)}")



    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")