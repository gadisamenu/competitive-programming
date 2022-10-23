class Solution:
    def minOperations(self, n: int) -> int:
        average = n
        operations = 0
        
        i = 1
        while i < n:
            operations += (average-i)
            i += 2
        return operations
            