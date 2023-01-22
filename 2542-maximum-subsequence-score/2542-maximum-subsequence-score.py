class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        nums = []
        for i in range(len(nums1)):
            nums.append([nums2[i],nums1[i]])
            
        nums.sort()
        heap = []
        
        index = len(nums1)
        _sum =  0
        while len(heap) < k:
            index -= 1
            _sum += nums[index][1]
            heappush(heap,nums[index][1])
            
     
        answer  = _sum*nums[index][0]

        while index > 0:
            index -= 1
            _sum += nums[index][1]
            heappush(heap,nums[index][1])
            _sum -= heappop(heap)
            answer = max(answer,_sum*nums[index][0])
            
        return answer
                
        
        
        