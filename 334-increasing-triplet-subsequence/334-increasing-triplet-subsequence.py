class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return  False
        first = float("inf")
        second = float("inf")
        
        for i  in range(0,len(nums)):
            if nums[i] < first:
                first = nums[i]
            elif nums[i]  < second and nums[i] != first:
                second = nums[i]
            elif nums[i] > second:
                return True
        return False
                
            
            
            
            