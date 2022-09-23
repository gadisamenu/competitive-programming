class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_s = defaultdict(int)
        prefix_s[0] += 1
        
        ans = 0
        _sum = 0
        for n in nums:
            _sum +=n
            ans += prefix_s[_sum-k]                
            prefix_s[_sum]+=1
        return ans