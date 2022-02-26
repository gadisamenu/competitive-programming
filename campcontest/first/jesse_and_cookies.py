#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'cookies' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY A
#

def cookies(k, A):
    # Write your code here
    # sweetness = []
    heapq.heapify(A)
    
    if  len(A)< 2:
        return -1
    iterr = 0
    while A[0] < k:
        if len(A) < 2:
            return -1
        first = heapq.heappop(A)
        second = heapq.heappop(A)
        heapq.heappush(A,(first+ 2*second))
        iterr += 1
        
    return iterr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
