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

DOPART1 = False
DOPART2 = True
DEBUG = True

with open('day09.txt') as datafile:
    alldata = datafile.readline().strip()

testdata = "2333133121414131402".strip()   # 


thedata = testdata
#thedata = alldata

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

def findFirstBlankBlock(disklist:list, startat=0) -> tuple[int, tuple]:
    for chunkID, ablock in enumerate(disklist[startat:]):
        if ablock[1] is None:
            return chunkID+startat, ablock
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

    firstBlankId, firstBlankBlock = findFirstBlankBlock(thedisk, startat=0)

    idEndblock = len(thedisk)-1
    while firstBlankId >= 0:
        endblock = thedisk[idEndblock]

        if idEndblock == firstBlankId:
            # we are done
            firstBlankId = -1

        if endblock[1] is None:
            thedisk.pop() # drop it
            idEndblock -= 1
        else:
            # okay this has stuff, try to find a place to put it

            if firstBlankBlock[0] > endblock[0]:
                # blank block has end space to hold it all, so insert the whole set ahead of this one
                firstBlankBlock = (firstBlankBlock[0] - endblock[0], None)
                thedisk[firstBlankId] = firstBlankBlock
                thedisk.insert( firstBlankId, endblock) 

                firstBlankId += 1 # id's need to be incremented
                idEndblock += 1
                thedisk.pop()
                idEndblock -= 1   # move on to the next    
                if firstBlankId >= len(thedisk):
                    firstBlankId = -1  # nothing left            
            else:
                # will exhaust all of the empty space in this blankblock
                blockspace = firstBlankBlock[0]
                thedisk[firstBlankId] = (blockspace, endblock[1])
                thedisk[-1] = (endblock[0] - blockspace, endblock[1])
                # find the next
                firstBlankId, firstBlankBlock = findFirstBlankBlock(thedisk, startat=firstBlankId)

        if DEBUG:
            print(f"after examining {idEndblock}, {thedisk}")

    checksum = calcChecksum(thedisk)
    print(f"Part 1:  checksum = {checksum}")



    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    thedisk = mapToList(thedata)

    if DEBUG:
        print(thedisk)

    firstBlankId, firstBlankBlock = findFirstBlankBlock(thedisk, startat=0)
    # move from left to right examing blank blocks to fill
    while firstBlankId >= 0:

        # look from the back to the front at files that could fit here
        for idfile in range(len(thedisk)-1, firstBlankId, -1):
            endblock = thedisk[idfile]
            if endblock[1] is not None:
                # this is file
                if firstBlankBlock[0] >= endblock[0]:
                    # there is enough room to fit this
                    remainingspace = firstBlankBlock[0] - endblock[0]

                    newendblock = (endblock[0], None)
                    thedisk[idfile] = newendblock
                    
                    if remainingspace > 0:
                        # save space of the old
                        firstBlankBlock = (remainingspace, None)
                        thedisk[firstBlankId] = firstBlankBlock
                        thedisk.insert(firstBlankId, endblock)
                    else:
                        # end of space
                        newendblock = (endblock[0], None)
                        thedisk[idfile] = newendblock
                        firstBlankBlock = endblock
                        thedisk[firstBlankId] = firstBlankBlock
                    
                    # got it
                    break
                    

        if DEBUG:
            print(f"after examining {firstBlankId}, {thedisk}")

        # maybe we did it, maybe not!  in any case, move on
        firstBlankId, firstBlankBlock = findFirstBlankBlock(thedisk, startat=firstBlankId)










    checksum = calcChecksum(thedisk)
    print(f"Part 2:  checksum = {checksum}")



    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")