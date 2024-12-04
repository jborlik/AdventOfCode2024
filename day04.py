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
DEBUG = False

with open('day04.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()]   # 


thedata = testdata
#thedata = alldata

width = len(thedata[0])
height = len(thedata)

THEWORD = 'XMAS'
directions = [(-1,-1),(0,-1),(1,-1),
              (-1,0),(1,0),
              (-1,1),(0,1),(1,1)]
# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def evaluateInDir( init_w, init_h, stepnum, theword, direction) -> bool:
    if stepnum == len(theword):
        return True
    iw = init_w + direction[0]*stepnum
    ih = init_h + direction[1]*stepnum
    if (iw < 0) or (ih < 0):
        return False
    if (iw >= width) or (ih >= height):
        return False
    if theword[stepnum] != thedata[ih][iw]:
        return False
    # okay, check the next
    return evaluateInDir(init_w, init_h, stepnum+1, theword, direction)
    


if DOPART1:

    START = time.perf_counter()

    count = 0
    for iw in range(width):
        for ih in range(height):
            if thedata[ih][iw] == THEWORD[0]:
                # potential match
                for adirection in directions:
                    gotone = evaluateInDir(iw,ih, 1, THEWORD, adirection)
                    if gotone and DEBUG:
                        print(f"Found at {iw},{ih} in direction {adirection}")
                    count += int(gotone)

    
    print(f"PART 1: found {count}")




    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

TEMPLATES = [
    { (-1,-1):'M', (1,-1):'S',
      (-1, 1):'M', (1, 1):'S' },
    { (-1,-1):'S', (1,-1):'S',
      (-1, 1):'M', (1, 1):'M' },
    { (-1,-1):'M', (1,-1):'M',
      (-1, 1):'S', (1, 1):'S' },
    { (-1,-1):'S', (1,-1):'M',
      (-1, 1):'S', (1, 1):'M' },
]

def checkTemplate(init_w, init_h, thetemplate) -> bool:
    if (init_w-1 < 0) or (init_h-1 < 0):
        return False
    if (init_w+1 >= width) or (init_h+1 >= height):
        return False
    
    for key, val in thetemplate.items():
        achar = thedata[ init_h + key[1] ][ init_w + key[0] ]
        if achar != val:
            return False
    return True


if DOPART2:
    START = time.perf_counter()

    count = 0
    for iw in range(width):
        for ih in range(height):
            if thedata[ih][iw] == 'A':
                # potential match
                for itemplate, atemplate in enumerate(TEMPLATES):
                    gotone = checkTemplate(iw,ih, atemplate)
                    if gotone and DEBUG:
                        print(f"Found at {iw},{ih} in template {itemplate}")
                    count += int(gotone)

    print(f"PART 2: found {count}")

    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")