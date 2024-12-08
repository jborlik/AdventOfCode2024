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
