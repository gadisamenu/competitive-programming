class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans=[]         
        
        for i in range(len(l)):
            value = True
            num = nums[l[i]:r[i]+1]
            num.sort()
            ran = num[1] - num[0]
            length = len(num)-1
            for ind in range(1,length):
                if num[ind+1]- num[ind] == ran:
                    pass
                else:
                    value = False
                    break
            ans.append(value)
        return ans
                