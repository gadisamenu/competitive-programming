class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        setted = set(nums)
        maxim = 0
        for num in nums:
            if (num-1) not in setted:
                cur=0
                nu =  num
                while nu in setted:
                    cur+=1
                    nu+=1
                maxim = max(cur,maxim)
        return maxim
                
        