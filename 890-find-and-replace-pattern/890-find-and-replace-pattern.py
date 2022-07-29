class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        replace = defaultdict(str)
        
        ans = []
        for word in words:
            failed = False
            for ind in range(len(word)):
                if pattern[ind] in replace:
                    
                    if replace[pattern[ind]] != word[ind]:
                        failed = True
                        break
                else:
                    replace[pattern[ind]]=word[ind]
            
            
            if not failed:
                val = replace.values()
                if len(val) == len(set(val)):
                    ans.append(word)
            replace.clear()
                
                
        return ans
            