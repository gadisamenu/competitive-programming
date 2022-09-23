class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        prefix[0] +=1
        _sum =0
        ans =0
        for n  in nums:
            _sum+= n
            m = _sum%k
            ans += prefix[m]
            prefix[m]+=1
            
        return ans