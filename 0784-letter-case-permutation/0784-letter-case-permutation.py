class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def recursion(i):
            if i >= len(s):
                answer.add("".join(s))
            else:
                s[i] = s[i].upper()
                recursion(i+1)
                s[i] = s[i].lower()
                recursion(i+1)
                
        answer = set()
        s = list(s)
        recursion(0)
        return answer
    

