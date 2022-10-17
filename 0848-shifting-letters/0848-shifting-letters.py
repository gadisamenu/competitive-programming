class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        
        for i in range(len(s)-1,0,-1):
            shifts[i-1]+=shifts[i]
            
        for i in range(len(s)):
            s[i] = string.ascii_lowercase[((ord(s[i])-97)+shifts[i])%26]
            
        return "".join(s)
            
        