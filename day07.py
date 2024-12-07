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

with open('day07.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()]   # 


thedata = testdata
thedata = alldata

# list of tuples, 0=target value, 1=list of constituents
thedata = [(int(x.split(':')[0]), list(map(int,x.split(':')[1].strip().split(' '))) ) for x in thedata ]

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def checkEquation(target, values, operations) -> tuple[int, list]:

    for checkconfig in itertools.product(operations, repeat=len(values)-1):
        equationvalue = values[0]
        for i,nextval in enumerate(values[1:]):
            if checkconfig[i]=='+':
                equationvalue += nextval
            elif checkconfig[i]=='*':
                equationvalue *= nextval
            elif checkconfig[i]=='|':
                equationvalue = int(str(equationvalue) + str(nextval))
        if equationvalue == target:
            if DEBUG:
                print(f"Found {equationvalue}: {checkconfig}")
            return target, checkconfig
    return 0, None

if DOPART1:

    START = time.perf_counter()

    operations = '+*'

    sum = 0
    for anequation in thedata:
        target = anequation[0]
        values = anequation[1]

        eqnval, eqnops = checkEquation(target, values, operations)
        sum += eqnval




    print(f"Part 1:  sum of good = {sum}")
        
        



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    operations = '+*|'

    sum = 0
    for anequation in thedata:
        target = anequation[0]
        values = anequation[1]

        eqnval, eqnops = checkEquation(target, values, operations)
        sum += eqnval

    print(f"Part 2:  sum of good = {sum}")
        
        

    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")