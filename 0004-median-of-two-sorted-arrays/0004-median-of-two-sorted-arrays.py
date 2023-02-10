class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half_merged = []
        length = len(nums1) + len(nums2)
        half_length = length//2 + 1
        
        while half_length and nums1 and nums2:
            if nums1[0] <= nums2[0]:
                half_merged.append(nums1.pop(0))
            else:
                half_merged.append(nums2.pop(0))
            half_length -=1
            
        if half_length:
            if nums1:
                half_merged.extend(nums1[:half_length])
            else:
                half_merged.extend(nums2[:half_length])
            
        if length%2 == 0:
            return (half_merged[-1] + half_merged[-2])/2 + 0.00000
        return half_merged[-1] + 0.00000
    
    
    
            