class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        result = self.merge_sort(nums)
        ans=''
        zeros = True
        for num in result:
            if num != 0:
                zeros = False
            ans += str(num)
            
        if zeros:
            return "0"
            
        return ans
        
    def merge_sort(self,nums):
        if len(nums) <=1:
            return nums
        
        left = self.merge_sort(nums[:len(nums)//2])
        right = self.merge_sort(nums[len(nums)//2:])
        
        return self.merge(left,right)
    
    def merge(self,left,right):
        result = []
        i = 0
        j = 0
        while i < len(left) and j < len(right):
            if int(str(left [i]) + str(right[j])) >= int(str(right[j]) + str(left[i])):
                result.append(left[i])
                i +=1
            else:
                result.append(right[j])
                j+=1
                
        if j < len(right):
            result.extend(right[j:])
        if i < len(left):
            result.extend(left[i:])
            
            
        return result