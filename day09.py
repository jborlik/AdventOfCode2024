#import itertools
#import numpy as np
#import copy
#import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field
from typing import Optional

DOPART1 = True
DOPART2 = True
DEBUG = False

with open('day09.txt') as datafile:
    alldata = datafile.readline().strip()

testdata = "2333133121414131402".strip()   # 


thedata = testdata
thedata = alldata

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def mapToList(textmap: str) -> list:
    """list of tuples ( count, [id:int or None])"""
    thelist = []
    nextIsBlank = False
    nextID = 0
    for achar in textmap:
        if nextIsBlank:
            rep = (int(achar), None)
        else:
            rep = (int(achar), nextID)
            nextID += 1
        nextIsBlank = not nextIsBlank
        if int(achar) != 0:
            thelist.append(rep)  #i.e. if zero just ignore it
    if thelist[-1][1] is None:
        thelist.pop()
    return thelist

def lengthOfList(disklist:list) -> int:
    count = 0
    for ablock in disklist:
        count += ablock[0]
    return count

def fileIDAtIndex(disklist:list, index:int) -> Optional[int]:
    count = 0
    for ablock in disklist:
        count += ablock[0]
        if index < count:
            return ablock[1]
    print(f"Huh?  requested ID={index} not in range")
    return None

def findFirstBlankBlock(disklist:list) -> tuple[int, tuple]:
    for chunkID, ablock in enumerate(disklist):
        if ablock[1] is None:
            return chunkID, ablock
    return -1, None  # not found?


def calcChecksum(disklist:list) -> int:
    checksum = 0
    startpos = 0
    for ablock in disklist:
        thischunk = 0
        for i in range(ablock[0]):
            ii = startpos + i
            if ablock[1]:
                thischunk += ii*ablock[1]
        checksum += thischunk
        startpos += ablock[0] 
    return checksum



if DOPART1:

    START = time.perf_counter()

    thedisk = mapToList(thedata)

    if DEBUG:
        print(thedisk)


    firstBlankId, firstBlankBlock = findFirstBlankBlock(thedisk)
    while (firstBlankBlock is not None) and (firstBlankId != (len(thedisk)-1) ) :
        # I have a blank block that could store stuff from the end
        remainingspace = firstBlankBlock[0]
        while remainingspace > 0:

            # so find the lastblock and take what you can from it
            lastblock = thedisk[-1]
            assert lastblock[1] is not None
            if firstBlankBlock[0] > lastblock[0]:
                # I have more space than the last block, so insert that whole set ahead of this one
                remainingspace -= lastblock[0]
                thedisk[firstBlankId] = (remainingspace, None)
                thedisk.insert( firstBlankId, lastblock)
                firstBlankId += 1
                thedisk.pop()
                while thedisk[-1][1] is None:
                    thedisk.pop()
            else:
                # I would exhaust the remaining space
                thedisk[firstBlankId] = (remainingspace, lastblock[1])
                thedisk[-1] = (lastblock[0] - remainingspace, lastblock[1])
                remainingspace = 0

        firstBlankId, firstBlankBlock = findFirstBlankBlock(thedisk)
        if DEBUG:
            print(thedisk)

    checksum = calcChecksum(thedisk)
    print(f"Part 1:  checksum = {checksum}")



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()




    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")