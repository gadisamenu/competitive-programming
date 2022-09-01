class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        indexs = {}
        for i,v in enumerate(nums1):
            indexs[v]= i
            
        ans = [-1 for x in range(len(nums1))]
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                vl = stack.pop()
                if vl in indexs:
                    ans[indexs[vl]] = num
            stack.append(num)
        return ans
            