class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        bits =[1 for i in range(32)]
        
        for i in range(32):
            num = right &~(1 << i)
            j = 0
            while num < left and  j < i:
                num |= 1 << j
                j+= 1
            if num >= left:
                bits[i] = 0
            i += 1
                
        ans = 0
        for i in range(32):
            if bits[i]:
                ans |= 1 << i
    
        return ans