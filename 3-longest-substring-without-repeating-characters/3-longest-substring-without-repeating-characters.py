class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        i , j = 0, 0 
        lgth = len(s)
        max_substr = 0
        
        while j < lgth:
            
            if s[j] in substring:
                max_substr = max(max_substr,j-i)
                substring.remove(s[i])
                i+=1
                
            else:
                substring.add(s[j])
                j+=1
                
        max_substr = max(max_substr,len(substring))
                
        return max_substr