#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#

def insertionSort1(n, arr):
    hold = arr[-1]
    # Write your code here
    n -= 2
    while n >= 0:
        if arr[n] > hold:
            arr[n + 1] = arr[n]
            print(*arr)
            if n ==0:
                arr[0] = hold
                print(*arr)
                break
            n -=1
        else:
            arr[n+1]=hold
            print(*arr)
            break

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
