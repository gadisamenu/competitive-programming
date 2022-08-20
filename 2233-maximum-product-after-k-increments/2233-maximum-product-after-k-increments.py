class Solution:
    def maximumProduct(self, nums: List[int], k: int) -> int:
        heapify(nums)
        while k:
            heappush(nums,heappop(nums)+1)
            k -= 1
        pro = 1
        for n in nums:
            pro = (pro * n)% 1000000007
            
        return pro % 1000000007
            