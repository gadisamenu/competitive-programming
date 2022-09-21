class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evens = 0
        for n in nums:
            if n%2 == 0:
                evens += n

        ans =  []
        for val,ind in queries:
            if nums[ind] %2 == 0:
                if val%2 == 0:
                    evens += val
                else:
                    evens -= nums[ind]
                    
            else:
                if val%2 != 0:
                    evens += (val+ nums[ind])                    
            ans.append(evens)
                
            nums[ind] += val
        return ans
                
            