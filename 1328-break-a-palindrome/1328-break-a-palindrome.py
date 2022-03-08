class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome) == 1:
            return ""
        
        lgth= len(palindrome)
        for i in range(lgth):
            if i == lgth//2 != lgth/2:
                continue
            if palindrome[i] != "a":
                return palindrome[:i]+"a"+palindrome[i+1:]
            elif i == lgth -1:
                return palindrome[:-1]+"b"

            