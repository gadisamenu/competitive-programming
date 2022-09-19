class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        for n  in nums:
            if nums[abs(n)-1] > 0: nums[abs(n)-1]*= -1
                    
        for i in range(len(nums)):
            if nums[i] >= 0:
                ans.append(i+1)
                
        return ans
        