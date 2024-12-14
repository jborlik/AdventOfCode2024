#import itertools
import numpy as np
#import copy
import re   # r = re.compile(r'xxx'), m = r.match(str), print(m[1])
#import collections  # including deque
#import math
import time
#import pprint
#from dataclasses import dataclass, field
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib.patches as patches

DOPART1 = False
DOPART2 = True
DODISPLAY = False
DEBUG = True

with open('day14.txt') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

testdata = [x.strip() for x in """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3""".splitlines()]   # 

#testdata = [x.strip() for x in """p=2,4 v=2,-3""".splitlines()]


thedata = testdata
thedata = alldata

width, height = 11, 7
width, height = 101, 103

re_inp =  re.compile(r'p=(-*\d+),(-*\d+) v=(-*\d+),(-*\d+)')

quadrants = width // 2, height // 2

class Robot:
    def __init__(self, aline:str):
        m = re_inp.match(aline)
        self.position = (int(m.group(1)), int(m.group(2)))
        self.vel = (int(m.group(3)), int(m.group(4)))
    
    def __repr__(self):
        return f"[p={self.position} v={self.vel} q={self.quadrant()}]"

    def step(self):
        self.position = (
            (self.position[0] + self.vel[0]) % width,
            (self.position[1] + self.vel[1]) % height,
        )
    def quadrant(self) -> int:
        if self.position[0] < quadrants[0]:
            # 2 or 3
            if self.position[1] < quadrants[1]:
                return 2
            elif self.position[1] > quadrants[1]:
                return 3
        elif self.position[0] > quadrants[0]:
            # 1 or 4
            if self.position[1] < quadrants[1]:
                return 1
            elif self.position[1] > quadrants[1]:
                return 4
        return 0
    def isarea(self, xfrom, xto, yfrom, yto) -> int:
        if self.position[0] >= xfrom and self.position[0] <= xto and self.position[1] >= yfrom and self.position[1] <= yto:
            return 1
        return 0


robots = [Robot(aline) for aline in thedata]

# ------------------------------------------------------------------------------------
#  Part 1
# ------------------------------------------------------------------------------------

if DOPART1:

    START = time.perf_counter()

    for itime in range(100):
        for arobot in robots:
            arobot.step()
    
    print(robots)

    quadcount = {}
    for arobot in robots:
        atquad = arobot.quadrant()
        quadcount[ atquad ] = quadcount.get(atquad, 0) + 1

    print(quadcount)
    sf = 1
    for iq, vq in quadcount.items():
        if iq != 0:
            sf *= vq
    
    print(f"Part 1: sf = {sf}")

    END = time.perf_counter()
    print(f"Time taken for part 1: {END - START} seconds")

# ------------------------------------------------------------------------------------
#  Part 2
# ------------------------------------------------------------------------------------

def printIt(robots):
    loc = {}
    for arobot in robots:
        loc[arobot.position] = loc.get(arobot.position,0) + 1
    # print
    for ih in range(height):
        for iw in range(width):
            if (iw,ih) in loc.keys():
                print('X',end='')
            else:
                print(' ',end='')
        print()
    print()

def checkNumInRow(loc, maxnuminrow=10) -> bool:
    numinrow = 0
    lastwason = False
    for ih in range(height):
        for iw in range(width):
            if (iw, ih) in loc.keys():
                # one here
                if lastwason:
                    numinrow += 1
                else:
                    lastwason = True
                    numinrow = 0

                if numinrow >= maxnuminrow:
                    return True
            else:
                lastwason = False
                numinrow = 0
        lastwason = False
        numinrow = 0
    return False

if DOPART2:

    for itime in range(100000):

        countintopleft = 0
        loc = {}
        for arobot in robots:
            arobot.step()
            loc[arobot.position] = loc.get(arobot.position,0) + 1
            
        if checkNumInRow(loc, 10):
            print(f"Found it?  {itime+1}")
            printIt(robots)
            break





    print(f"Part 2: maybe at {itime+1}")



# ------------------------------------------------------------------------------------
#  DISPLAY for Part 2
# ------------------------------------------------------------------------------------

if DODISPLAY:
    START = time.perf_counter()

    MAXCOUNT = 271

    fig, ax = plt.subplots()
    circles = []
    frametext = ax.text(0,-10, 't=0')

    for arobot in robots:
        ac = ax.add_patch(patches.Circle(arobot.position, radius=1))
        circles.append(ac)
    ax.set(xlim=[0, width], ylim=[-10, height])

    icount = 0

    def on_press(event):
        if event.key.isspace():
            if anim.running:
                anim.event_source.stop()
            else:
                anim.event_source.start()
            anim.running ^= True
        elif event.key == 'left':
            anim.direction = -1
        elif event.key == 'right':
            anim.direction = +1

        # Manually update the plot
        if event.key in ['left','right']:
            t = anim.frame_seq.__next__()
            update(t)
            plt.draw()


    def update(frame):
        for arobot,acircle in zip(robots,circles):
            arobot.step()
            acircle.set(center=arobot.position)

        global icount
        icount += 1

        frametext.set(text=f"t={icount}")        
        artists = circles.copy()
        artists.append(frametext)
        return circles
    
    fig.canvas.mpl_connect('key_press_event', on_press)  

    anim = animation.FuncAnimation(fig=fig, func=update, frames=MAXCOUNT, repeat=False)
    anim.running = True
    anim.direction = +1
    
    plt.show()
                




    END = time.perf_counter()
    print(f"Time taken for part 2: {END - START} seconds")