#import itertools
#import numpy as np
#import copy
import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

DOPART1 = True
DOPART2 = True

with open('day03.txt') as datafile:
    alldata = datafile.read()

testdata = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"   # 
testdata = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"   # 


thedata = testdata
thedata = alldata


r = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')
r_enable = re.compile(r'do\(\)')
r_disable = re.compile(r'don\'t\(\)')


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if DOPART1:

    START = time.perf_counter()

    m = r.findall(thedata)
    sum = 0
    for am in m:
        thismul = int(am[0])*int(am[1])
        sum += thismul

    print(f"Part 1: sum={sum}")



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    iat = 0
    sum = 0
    enabled = True

    while iat < len(thedata):

        #thistext = thedata[iat:]

        im, ien, idis = len(thedata), len(thedata), len(thedata)

        mm = r.search(thedata,iat)
        menable = r_enable.search(thedata,iat)
        mdisable = r_disable.search(thedata,iat)
        
        if mm:
            im = mm.start()
        if menable:
            ien = menable.start()
        if mdisable:
            idis = mdisable.start()
        
        if (im < ien) and (im < idis):
            # first match is mul(x,y)
            print(f"mul match at {im} (enabled={enabled}): {mm}")
            if enabled:
                thismul = int(mm.group(1))*int(mm.group(2))  # search returns first
                sum += thismul
            iat = im + 1
        
        if (ien < im) and (ien < idis):
            # first match is "enable"
            enabled = True
            print(f"enabled at {ien}")
            iat = ien + 1
        
        if (idis < im) and (idis < ien):
            print(f"disnabled at {idis}")
            enabled = False
            iat = idis + 1

        # nothing found?
        if (im == ien) and (im == idis):
            iat = len(thedata)
        

    print(f"Part 2: sum={sum}")



    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")