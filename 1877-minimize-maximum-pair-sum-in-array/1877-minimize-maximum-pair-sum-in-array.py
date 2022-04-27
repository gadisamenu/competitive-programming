class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        lgth = len(nums)//2
        nums.sort()
        _max = 0
        for idx in range(lgth):
            pair = nums[idx] + nums[-(idx+1)]
            if _max < pair:_max = pair
        return _max