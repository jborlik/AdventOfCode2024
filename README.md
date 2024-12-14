# AdventOfCode2022
Python code to solve daily puzzles of http://adventofcode.com/2024

Code is tested with Python 3.11.4 (Anaconda distribution) on Win11. Developed with VSCode.

## Days

* Day 1:  Comparing two lists, part 1 sorted, part 2 via unique dicts.
* Day 2:  Checking differences in an integer array.
* Day 3:  Part 1 was a simple regex match with findall.  Part 2 had an "enabled/disabled" state in the string, so I ended up switching to a looped processing (still with regexes, but comparing which of the three keywords showed up sooner).
* Day 4:  Part 1 was a word search, so used the typical algorithm of "find the first letter, then check each direction".  Part 2 was not a word but rather letters in 2D shape.  There were few permutations, so I just looked for each of them.
* Day 5:  Part 1 used itertools to loop over each page pair, to check against a set of rules.  Part 2 was the reverse, where one needed to use the rules to order the set... In this case, I used functools.cmp_to_key, which made it straightforward.
* Day 6:  Classic AoC with walking/rotating direction of character in a maze. Part 1 was checking unique places visited in a walk.  Part 2 was trickier, in that one was trying to find alterations to the maze that resulted in a loop.  My "loop detection" algorithm was to check if the character already walked that space heading in the same direction.  And then I brute-forced it.  It took less than a minute to run (which is sort of long by AoC standards).
* Day 7:  Choose +/-/- ops to make a formula match a value.  Itertools.product() did the job.
* Day 8:  Look at pairs of points on grid, and extend their distance.  More itertools, this time combinations().
* Day 9:  "Defragging a disk".  Lots of list operations.  Part 1: Needed to go last to first, but basically brute force.  Part 2: Sort of the same, and barely got it in under 24 hours.  Not pretty.
* Day 10:  Organize paths into a directed graph.  I did part 2 (counting unique paths) before part 1 (counting unique endpoints), because I had misread the part 1 criterion.
* Day 11:  Process a list with a set of rules to make a new list, then iterate that a bunch of times.  The naive approach worked fine for Part 1, but Part 2 wanted more iterations which resulted in exploding the execution time.  Got a little help from Reddit, to point me in the right direction:  The order of the numbers didn't matter at all, so one could use a dictionary of the count of instances for a number.
* Day 12: TODO.  Got part 1 working, allocating tiles to areas, and determining the borders.  Part 2 is trickier... some borders are grouped.
* Day 13:  Part 1, could be brute-force searched (nested loops).  Part 2 required more thought.  Used numpy linalg solver (two linear equations, two unknowns!), but the trick was checking if the results were integers or not. This required some tolerancing.  I think that there are integer algorithms for this, as it is a system of linear Diophantine equations.  But I lucked out with floating-point tolerancing.
* Day 14:  Updating position of robots, based on constant velocity.  Part 1 required finding ways to group them by position, fairly easy.


## See previous work at:
* https://github.com/jborlik/AdventOfCode2015
* https://github.com/jborlik/AdventOfCode2016
* https://github.com/jborlik/AdventOfCode2017
* https://github.com/jborlik/AdventOfCode2018
* https://github.com/jborlik/AdventOfCode2019
* https://github.com/jborlik/AdventOfCode2020
* https://github.com/jborlik/AdventOfCode2021
* https://github.com/jborlik/AdventOfCode2022
* https://github.com/jborlik/AdventOfCode2023
