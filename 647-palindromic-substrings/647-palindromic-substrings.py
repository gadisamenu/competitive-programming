class Solution:
    def countSubstrings(self, s: str) -> int:
        def check(i,j):
            while  i>= 0 and j < len(s):
                if s[i] != s[j]:
                    break
                ans.add((i,j))
                i -= 1
                j += 1
            return i,j
        
        ans = set()
        for i in range(len(s)):
            check(i,i)
            check(i,i+1)
        return len(ans)
            