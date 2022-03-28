class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lgth = len(s)+1
        discovered = set()
        ans = set()
        i = 0 
        j = 10
        while j < lgth:
            if s[i:j] in discovered:
                ans.add(s[i:j])
            else:
                discovered.add(s[i:j])            
            i+=1
            j+=1
        return ans
                