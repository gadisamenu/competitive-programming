class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right= max(piles)
        
        best = right
        while left <= right:
            md = left + (right-left)//2
            
            hour = 0
            for pile in piles:
                hour += ceil(pile/ md)
                    
            if hour <= h:
                best = md
                right = md -1
            else:
                left = md + 1
                
                
        return best