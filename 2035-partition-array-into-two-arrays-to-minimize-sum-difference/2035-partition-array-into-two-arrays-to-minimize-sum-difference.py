class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        half = len(nums)//2
        left = nums[:half]
        right = nums[half:]
        left_sum = sum(left)
        right_sum = sum(right)
        
        ans = inf
        for i in range(half+1): 
            vals = sorted(2*sum(combo)-left_sum for combo in combinations(left, i))
            for combo in combinations(right, half-i): 
                diff = 2*sum(combo) - right_sum
                k = bisect_left(vals, -diff)
                if k: ans = min(ans, abs(vals[k-1] + diff))
                if k < len(vals): ans = min(ans, abs(vals[k] + diff))
                    
        return ans