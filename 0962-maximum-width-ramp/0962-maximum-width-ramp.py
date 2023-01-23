class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        starts = [(nums[0],0)]
        answer = 0 
        for i in range(1,len(nums)):
            if nums[i] < starts[-1][0]:
                starts.append((nums[i],i))
            else:
                index = self.binarySearch(starts,nums[i])
                answer = max(answer,i - index)
                
        return answer
                
       
    def binarySearch(self,array,target):
        left = 0
        right = len(array) -1
        while left < right:
            mdl = left + (right-left)//2
            if array[mdl][0] > target:
                left = mdl + 1
            else:
                right = mdl

        return array[right][1]
            