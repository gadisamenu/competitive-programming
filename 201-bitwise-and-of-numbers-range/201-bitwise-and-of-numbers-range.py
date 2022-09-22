class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        ans = 0
        num = right
        j = 0
        for i in range(32):
            num = num &~(1 << i)
            while num < left and  j < i:
                num |= 1 << j
                j+= 1
            if num < left:
                ans |= 1 << i
            i += 1
    
        return ans