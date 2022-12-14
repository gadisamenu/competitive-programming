class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) > 1:
            for i in range(len(nums)-3,-1,-1):
                nums[i] = max(nums[i+1],nums[i+2]+nums[i])
                if nums[i+1] < nums[i+2]:
                    nums[i+1] = nums[i+2]

            nums[0] = max(nums[0],nums[1])
        return nums[0]
            