class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        answer = set()
        divisibility  = []
        for num in nums:
            if num%p:
                divisibility.append(0)
            else:
                divisibility.append(1)
                
        for start in range(len(nums)):
            count = 0
            for i in range(start,len(nums)):
                if divisibility[i]:
                    count +=1 
                if count > k:
                    break
                answer.add(tuple(nums[start:i+1]))
                
        return len(answer)
            
        