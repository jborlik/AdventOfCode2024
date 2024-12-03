#import itertools
import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

DOPART1 = True
DOPART2 = True

with open('day02.txt') as datafile:
    alldata = [list(map(int,x.strip().split())) for x in datafile.readlines()]

testdata = [list(map(int,x.strip().split())) for x in """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()]   # 


thedata = testdata
thedata = alldata

def issafe(report):
    diff = np.diff(report)
    allincreasing = np.all(diff > 0)
    alldecreasing = np.all(diff < 0)
    absdiff = np.abs(diff)
    slowchange = np.all( (absdiff >= 1) & (absdiff <=3)  )
    return (allincreasing or alldecreasing) and slowchange

def issafe_dampened(report):
    if issafe(report):
        return True
    
    # okay, not safe, try removing one by one
    for i1 in range(len(report)):
        newreport = report.copy()
        del newreport[i1]
        if issafe(newreport):
            return True
    
    return False

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if DOPART1:

    START = time.perf_counter()

    numsafe = 0
    for areport in thedata:
        numsafe += issafe(areport)

    print(f"Part 1:  numsafe = {numsafe}")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    numsafe = 0
    for areport in thedata:
        numsafe += issafe_dampened(areport)

    print(f"Part 2:  numsafe = {numsafe}")



    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")