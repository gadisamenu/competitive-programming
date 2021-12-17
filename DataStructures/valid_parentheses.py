class Solution:
    def isValid(self, s: str) -> bool:
        state = True
        parentheses= { '(':')','{':'}','[':']'}
        opening=[]
        for brace in s:
            if brace in parentheses:
                opening.append(brace)
            else:
                if not opening:
                    return False
                if brace == parentheses[opening[-1]]:
                    opening.pop()
                else:
                    return False
        if opening:
            state = False
        return state