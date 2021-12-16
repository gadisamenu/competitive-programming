class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            ind = i
            for j in range(i-1,-1,-1):
                if nums[j] > nums[ind]:
                    nums[j],nums[ind] = nums[ind],nums[j]
                    ind -= 1
        return nums
            