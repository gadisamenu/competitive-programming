class Solution:
    def canJump(self, nums: List[int]) -> bool:
        my_jumps = nums[0]
        
        for ind in range(len(nums)-1):
            my_jumps = max(nums[ind],my_jumps)
            if not my_jumps: return False
            my_jumps -= 1
            
        return True
            