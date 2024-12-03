class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        
        for i in range(len(nums1)):
            heappush(heap,(nums1[i]+nums2[0],i,0))
            
        answer = []
        while len(answer) < k:
            _,ind_1,ind_2 = heappop(heap)
            answer.append((nums1[ind_1],nums2[ind_2]))
            if ind_2 + 1 < len(nums2):
                ind_2 += 1
                heappush(heap,(nums1[ind_1]+ nums2[ind_2],ind_1,ind_2))
                         
        return answer
                       
            

        
        