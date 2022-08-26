class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        ans = []
        while a + b > 0:
            if a >= b and (len(ans) < 2 or ans[-1] != "a" or ans[-2] != "a"):
                ans.append("a")
                a -= 1
            elif len(ans) < 2 or ans[-1] != "b" or ans[-2] != "b":
                ans.append("b")
                b -= 1
            else:
                ans.append("a")
                a -= 1
                
        return "".join(ans)
        