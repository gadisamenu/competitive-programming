class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if len(nums[i]) + len(nums[j]) == len(target):
                    if self.equal(nums[i]+nums[j],target):
                        answer += 1
                    if self.equal(nums[j]+ nums[i],target):
                        answer += 1
                        
        return answer
    
    def equal(self,num,target):
        for i in range(len(target)):
            if num[i] != target[i]:
                return 0
        return 1
   