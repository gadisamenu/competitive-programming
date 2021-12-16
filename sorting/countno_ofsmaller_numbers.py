class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lesses =[]
        nums_copy = nums[:]
        nums.sort()
        length = len(nums_copy)
        for i  in range(length):
            lesses.append(len(nums[:nums.index(nums_copy[i])]))
        return lesses

        