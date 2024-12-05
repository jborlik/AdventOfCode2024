import itertools
import functools
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

with open('day05.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()]   # 


thedata = testdata
thedata = alldata

rules = []
updates = []

iamparsingrules = True
for aline in thedata:
    if aline == "":
        iamparsingrules = False
    else:
        if iamparsingrules:
            rules.append( tuple(map(int, aline.split("|"))) )
        else:
            updates.append( list(map(int, aline.split(','))))


# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

def pairIsOrdered(firstpage, secondpage, rules) -> bool:
    # check for rule first|second (a good rule)
    if (firstpage,secondpage) in rules:
        return True
    if (secondpage,firstpage) in rules:
        return False 
       
    # if there is no rule?
    return True
    

def isCorrectOrdered(anupdate, rules) -> bool:
    # Can I do this in one pass? 
    for firstpage,secondpage in itertools.combinations(anupdate, 2):
        if not pairIsOrdered(firstpage,secondpage,rules):
            return False
    return True



if DOPART1:

    START = time.perf_counter()

    sum = 0
    for anupdate in updates:
        if isCorrectOrdered(anupdate, rules):
            thisone = anupdate[ (len(anupdate) - 1)//2  ]
            if DEBUG: 
                print(f"good: {thisone}")
            sum += thisone

    print(f"Part 1: sum = {sum}")
    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

def pairComparison(firstpage, secondpage) -> int:
    """ Comparison function,  +1 firstpage>secondpage, -1 firstpage<secondpage, 0="""
    # check for rule first|second (a good rule)
    if (firstpage,secondpage) in rules:
        return 1
    if (secondpage,firstpage) in rules:
        return -1       
    # if there is no rule?
    return 0

if DOPART2:
    START = time.perf_counter()

    sum = 0
    for anupdate in updates:
        if not isCorrectOrdered(anupdate, rules):
            newupdate = sorted(anupdate, key=functools.cmp_to_key(pairComparison), reverse=True)
            thisone = newupdate[ (len(newupdate) -1)//2]
            if DEBUG:
                print(f"resorting mid={thisone}: {newupdate}")
            sum += thisone

    print(f"Part 2: sum = {sum}")


    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")