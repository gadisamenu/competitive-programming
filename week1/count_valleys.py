#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def countingValleys(steps, path):
    # Write your code here
    length2= len(path)
    i= 0
    alt = 0
    # valley = False
    count_valley = 0
    while i < steps:
        if path[i] == 'D':
            alt -= 1
        if path[i] == 'U':
            if alt == -1:
                count_valley += 1
            alt +=1
        i += 1
    return count_valley      

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    steps = int(input().strip())

    path = input()

    result = countingValleys(steps, path)

    fptr.write(str(result) + '\n')

    fptr.close()
