class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        # heapify(nums)
        heap = []
        for n in nums:
            heappush(heap,-n)
        score = 0
        while k and nums:
            num = -heappop(heap)
            score += num
            num = ceil(num/3)
            if num:
                heappush(heap,-num)
            k-=1
        return score