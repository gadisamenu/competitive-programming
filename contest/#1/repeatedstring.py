#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'repeatedString' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    # Write your code here
    count = []
    times =1
    if n >= len(s):
        times = n//len(s)
        over = n - times* len(s)
        for id in range(len(s)):
            if s[id] == 'a':
                count.append(id)
    else:
        for id in range(n):
            if s[id] == 'a':
                count.append(id)
        return len(count)
    if n == times*len(s):
        return len(count)*times
    else:
        add =0
        for nu in count:
            if nu < over:
                add+=1
        return len(count)*times + add


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
