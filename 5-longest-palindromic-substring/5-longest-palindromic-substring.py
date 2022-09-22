class Solution:
    def longestPalindrome(self, s: str) -> str:
        def check(i,j):
            while  i>= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                i -= 1
                j += 1
            return i,j
        
        _max = 0
        pair = [0,1]
        
        for i in range(len(s)):
            ret = check(i,i)
            if _max < (ret[1] - ret[0]): 
                _max = (ret[1]-ret[0])
                pair = ret
            ret = check(i,i+1)
            if _max < (ret[1] - ret[0]): 
                _max = (ret[1]-ret[0])
                pair = ret
                
        return s[pair[0]+1:pair[1]]
            