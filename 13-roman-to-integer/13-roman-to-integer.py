class Solution:
    def romanToInt(self, s: str) -> int:
        value = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        pre = "M"
        integer = 0
        for char in s:
            if value[char] > value[pre]:
                integer += (value[char]-2*value[pre])
                
            else:
                integer+= value[char]
            pre = char
        return integer
                
            