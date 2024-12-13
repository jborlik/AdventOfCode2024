import itertools
import numpy as np
import sympy
#import copy
import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field

DOPART1 = False
DOPART2 = True
DEBUG = True

with open('day13.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """Button A: X+94, Y+34
Button B: X+22, Y+67
Prize: X=8400, Y=5400

Button A: X+26, Y+66
Button B: X+67, Y+21
Prize: X=12748, Y=12176

Button A: X+17, Y+86
Button B: X+84, Y+37
Prize: X=7870, Y=6450

Button A: X+69, Y+23
Button B: X+27, Y+71
Prize: X=18641, Y=10279""".splitlines()]   # 


thedata = testdata
thedata = alldata

r_butt = re.compile(r'X\+(\d+), Y\+(\d+)') #, m = r.match(str), print(m[1])
r_priz = re.compile(r'X=(\d+), Y=(\d+)')

class Machine:
    def __init__(self, inputlines:list):
        b1 = r_butt.search(inputlines[0])
        b2 = r_butt.search(inputlines[1])
        l = r_priz.search(inputlines[2])
        self.A = (int(b1.group(1)), int(b1.group(2)))
        self.B = (int(b2.group(1)), int(b2.group(2)))
        self.prize = (int(l.group(1)), int(l.group(2)))

    def __repr__(self):
        return f"[A:{self.A}, B:{self.B}, loc={self.prize}]"
    
    def findPresses(self):
        for pressA in range(MAXBUTTON):
            for pressB in range(MAXBUTTON):
                value = ( pressA*self.A[0] + pressB*self.B[0],
                          pressA*self.A[1] + pressB*self.B[1])
                if value[0]==self.prize[0] and value[1]==self.prize[1]:
                    self.presses = (pressA, pressB)
                    thiscost = pressA*COST_A + pressB*COST_B
                    return thiscost
        return None    # not found
    
    def findPressesLinAlg(self):
        #from sympy import Matrix, lcm
        #am = Matrix([ [self.A[0], self.B[0]], [self.A[1], self.B[1]] ])
        am = np.array([ [self.A[0], self.B[0]], [self.A[1], self.B[1]] ])
        bm = np.array([self.prize[0], self.prize[1]])
        try:
            x = np.linalg.solve(am,bm)
            xint = np.rint(x)
            xdiff = x - xint
            if np.all( np.abs(xdiff) < 1e-4 ):
                self.presses = (int(xint[0]), int(xint[1]) )
                thiscost = self.presses[0]*COST_A + self.presses[1]*COST_B
                return thiscost
            else:
                return None 
        except:
            return None
        
        

# no itertools.batched in python 3.11, :(
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)

machines = []
for fourlines in grouper(thedata, 4):
    machines.append( Machine(fourlines) )


MAXBUTTON = 100
COST_A = 3
COST_B = 1

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if DOPART1:

    START = time.perf_counter()

    totcost = 0
    for machine in machines:
        thiscost = machine.findPressesLinAlg()
        if thiscost:
            if DEBUG:
                print(f"Found {machine.presses} -> cost={thiscost}")
            totcost += thiscost

    print(f"Part 1:  Total cost= {totcost}")


    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")


# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

if DOPART2:
    START = time.perf_counter()

    for machine in machines:
        machine.prize = (machine.prize[0] + 10000000000000, machine.prize[1] + 10000000000000)

    totcost = 0
    for im, machine in enumerate(machines):
        thiscost = machine.findPressesLinAlg()
        if thiscost:
            if DEBUG:
                print(f"Found {im}: {machine.presses} -> cost={thiscost}")
            totcost += thiscost

    print(f"Part 2:  Total cost= {totcost}")

    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")