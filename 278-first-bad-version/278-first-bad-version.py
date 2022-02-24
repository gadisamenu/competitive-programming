# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n 
        bad  = 1
        
        while left <= right:
            m = left + (right-left)//2
            
            if isBadVersion(m):
                bad = m
                right = m - 1
                
            else:
                left = m + 1
                
        return bad
                