#!/bin/python3

import math
import os
import random
import re
import sys
import heapq

#
# Complete the 'runningMedian' function below.
#
# The function is expected to return a DOUBLE_ARRAY.
# The function accepts INTEGER_ARRAY a as parameter.
#

def runningMedian(a):
    # Write your code here
    medians = []
    maxHeap = []
    minHeap = []

    for num in a:
        if len(maxHeap) == len(minHeap):
            if not maxHeap and not minHeap:
                heapq.heappush(maxHeap,-num)
                medians.append(-maxHeap[0])
            else:
                if -maxHeap[0] > num:
                    heapq.heappush(maxHeap,-num)
                    medians.append(-maxHeap[0])
                else:
                    heapq.heappush(minHeap,num)
                    medians.append(minHeap[0])
                    
        elif len(maxHeap) > len(minHeap):
            if -maxHeap[0] > num:
                heapq.heappush(minHeap,-heapq.heapreplace(maxHeap,-num))
            else:
                heapq.heappush(minHeap,num)
            medians.append((-maxHeap[0]+ minHeap[0])/2)
        else:
            if minHeap[0] < num:
                heapq.heappush(maxHeap,-heapq.heapreplace(minHeap,num))
            else:
                heapq.heappush(maxHeap,-num)
            medians.append((-maxHeap[0]+ minHeap[0])/2)
    return medians

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    result = runningMedian(a)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
