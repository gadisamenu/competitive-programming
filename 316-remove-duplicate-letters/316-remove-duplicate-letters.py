class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        chars= set()
        dups = Counter(s)
        ans = []

        for c in s:
            if c not in chars:
                while ans and dups[ans[-1]]>1:
                    if ans[-1] > c:
                        chars.remove(ans[-1])
                        dups[ans.pop()]-=1
                    else: break
                ans.append(c)
                chars.add(c)
            else:
                dups[c]-=1
        return "".join(ans)
            
       
                
            
             