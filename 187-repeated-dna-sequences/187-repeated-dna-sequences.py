class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lgth = len(s)+1
        discovered = set()
        ans = []
        i = 0 
        j = 10
        while j < lgth:
            if s[i:j] in discovered:
                if s[i:j] not in ans: ans.append(s[i:j])
            else:
                discovered.add(s[i:j])            
            i+=1
            j+=1
        return ans
                