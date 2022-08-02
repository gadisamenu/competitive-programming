class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
    
        keep = 0
        digits[-1] += 1
        
        for n in range(1,len(digits)+1):
            digits[-n] += keep
            keep = 0
    

            if digits[-n]  > 9:
                keep = digits[-n]// 10
                digits[-n] %= 10
            else:
                return digits


        if keep >  0:
            ans = list(map(int,str(keep)))
            ans.extend(digits)
            return ans
        return digits
                
                
                
        
            