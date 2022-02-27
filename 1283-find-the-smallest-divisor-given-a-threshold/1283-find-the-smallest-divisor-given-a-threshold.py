class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left = 1
        right = max(nums)
        divisor = right
        while left <= right:
            try_divisor  = left + (right - left)//2
            sum_nums = 0
            for num in nums:
                sum_nums += ceil(num/try_divisor)
                
            if sum_nums <= threshold:
                divisor = try_divisor
                right = try_divisor-1
            else:
                left = try_divisor +1
                
                
        return divisor