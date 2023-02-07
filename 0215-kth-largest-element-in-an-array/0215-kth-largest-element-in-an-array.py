class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        indx_caliber = 10000
        
        lgth = 2*indx_caliber + 1
        count = [0 for _ in range(lgth)]
        
        for n in nums:
            count[n+indx_caliber]+= 1
     
        
        index = lgth-1
        while k:
            k -= min(k,count[index])
            index -= 1
    
            
        return index  + 1 - indx_caliber
        
        
        
                
        