class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        lgth = len(nums)
        nums.sort()
        ans = 0
        for i in range(lgth):
            if nums[i] == 0:
                continue
            for j in range(i+1,lgth):
                targ = nums[j]+nums[i]-1
                ind = min(bisect_right(nums,targ,j+1), lgth-1)
                if nums[ind] > targ: ind -= 1
                ans += ind - j
                
        return ans