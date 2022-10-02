from sortedcontainers import SortedList
class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k: return False
        
        count  = Counter(nums)
        sorted_l = SortedList(count.keys())
        num_groups = len(nums)//k
        
        
        while num_groups:
            mov = 0
            for i in range(k):
                if i  == k-1 or (len(sorted_l) > i+1+mov and sorted_l[i+1+mov] - sorted_l[i+mov] == 1):
                    
                    if count[sorted_l[i+mov]] == 1:
                        sorted_l.pop(i+mov)
                        mov -= 1
                        
                    else: count[sorted_l[i+mov]] -=1
                        
                else: return False
                    
            num_groups -= 1
            
        return True
        