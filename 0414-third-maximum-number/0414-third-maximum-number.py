class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = list(set(nums))
        
        if len(nums) < 3:
            return max(nums)

        for i in range(len(nums)):
            nums[i]*= -1
                    
        heapify(nums)
     
        k = 3
        while k:
            answer = heappop(nums)
            k -= 1
            
        return -answer
        