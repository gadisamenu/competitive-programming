#User function Template for python3

class Solution:
    #Heapify function to maintain heap property.
    def heapify(self,arr, n, i):
        # code here0
        while i < n:
            if self.getleft(i) < n and self.getright(i) < n:
                minind = self.getright(i) if arr[self.getright(i)] < arr[self.getleft(i)] else self.getleft(i)
                if arr[i] > arr[minind]:
                    arr[i],arr[minind] = arr[minind],arr[i]
                    i = minind
                else:
                    break
                
            elif self.getleft(i) < n:
                if arr[i] > arr[self.getleft(i)]:
                    arr[i],arr[self.getleft(i)] = arr[self.getleft(i)],arr[i]
                break
            else:
                break
        
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        #code here
        i = n-1
        while i+1:
            if self.getleft(i) < n and self.getright(i) < n:
                minind = self.getright(i) if arr[self.getright(i)] < arr[self.getleft(i)] else self.getleft(i)
                if arr[i] > arr[minind]:
                    arr[i],arr[minind] = arr[minind],arr[i]
                    j = minind
                    self.heapify(arr,n,j)
                    
                    
            elif self.getleft(i) < n:
                if arr[i] > arr[self.getleft(i)]:
                    arr[i],arr[self.getleft(i)] = arr[self.getleft(i)],arr[i]
                    
            i-=1
    
            
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        #code here'
        lgth = len(arr)
        self.buildHeap(arr,n)
        # if lgth > 1:
            
        i = 1
        while i < lgth:
            arr[0],arr[lgth-i] = arr[lgth-i],arr[0]
            j = 0
            self.heapify(arr,lgth-i,j)
            
            i += 1
                    
        arr.reverse()
    
    
    def getleft(self,i):
        return 2* i + 1
    def getright(self,i):
        return 2*i + 2
        
#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().HeapSort(arr,n)
        print(*arr)

# } Driver Code Ends