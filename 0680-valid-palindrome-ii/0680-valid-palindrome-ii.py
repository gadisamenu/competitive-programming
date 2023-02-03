class Solution:
    def validPalindrome(self, s: str,used=False) -> bool:
        i = 0
        j = len(s) -1
        
        while i < j:
            if s[i] != s[j]:
                if used:
                    return False
                return self.validPalindrome(s[i:j],True) or self.validPalindrome(s[i+1:j+1],True)
            i += 1
            j -= 1
        return True

                    