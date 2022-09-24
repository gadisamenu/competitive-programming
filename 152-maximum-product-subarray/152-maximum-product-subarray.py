class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        _max_cur = nums[0]
        _min_cur = nums[0]
        _maxim = nums[0]
    
        for i in range(1,len(nums)):
            temp = max(_max_cur*nums[i], _min_cur*nums[i], nums[i])
            _min_cur = min(_max_cur*nums[i],_min_cur*nums[i],nums[i])
            _max_cur = temp
            _maxim = max(_maxim,_max_cur)
        return _maxim