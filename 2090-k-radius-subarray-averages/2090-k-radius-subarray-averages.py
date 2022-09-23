class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        ans = [-1 for i in range(len(nums))]
        width = 2*k+ 1
        
        if width > len(nums): return ans
        _sum = 0
        
        for i in range(width):
            _sum += nums[i]
        
        i= 0
        j = width -1
        while  True:
            ans[i+k] = _sum //width
            _sum -= nums[i]
            i+=1
            j += 1
            if  j >= len(nums):break
            _sum += nums[j]
            
        return ans
