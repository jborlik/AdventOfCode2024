#import itertools
import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

DOPART1 = False
DOPART2 = True

with open('day01.txt') as datafile:
    alldata = [list(map(int,x.strip().split())) for x in datafile.readlines()]

testdata = [list(map(int,x.strip().split())) for x in """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()]   # 


thedata = testdata
thedata = alldata

thedata = np.array(thedata)


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if DOPART1:

    START = time.perf_counter()

    l1 = np.sort(thedata[:,0])
    l2 = np.sort(thedata[:,1])

    sum = 0
    for a1,a2 in zip(l1,l2):
        thisgroup = abs(a1-a2)
        sum += thisgroup
    
    print(f"Part 1: sum={sum}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

START = time.perf_counter()

if DOPART2:
    l1 = thedata[:,0]
    l2 = thedata[:,1]

    sum = 0

    unique, counts = np.unique(l2, return_counts=True)
    uniquedict = dict(zip(unique, counts))

    for aval in l1:

        thisscore = aval * uniquedict.get(aval,0)        
        sum += thisscore

    print(f"Part 2: sum = {sum}")

END = time.perf_counter()
print(f"Time taken for part 2: {END - START} seconds")