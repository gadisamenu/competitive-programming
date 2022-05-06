class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle = list(needle)
        haystack = list(haystack)
        
        i = 0
        j = len(needle)-1
        while j < len(haystack):
            if needle[0] == haystack[i]:
                m = 0
                for n in range(1,len(needle)):
                    if needle[n] != haystack[i+n]:
                        break
                    m = n
                if m == len(needle)-1: return i
            i+=1
            j+=1
        return -1
        