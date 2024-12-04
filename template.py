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
DEBUG = True

with open('day17.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12""".splitlines()]   # 


thedata = testdata
#thedata = alldata

directions = [(-1,-1),(0,-1),(1,-1),
              (-1,0),        (1,0),
              (-1,1), (0,1), (1,1)]

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if DOPART1:

    START = time.perf_counter()


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()




    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")