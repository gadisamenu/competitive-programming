class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            
        nums.sort()
        moves = 0
        for n in range(len(nums)):
            over = count[nums[n]] - 1
            if over > 0:
                
                count[nums[n]+1] += over
                moves += over
                if n+1 < len(nums):
                    nums[n+1] = nums[n]+1
                
        return moves
                     
        
        