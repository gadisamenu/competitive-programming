class Solution:
    def calculate(self, s: str) -> int:
        ans = [0]
        add = True
        num = ["0"]
        mult = []
        for ind in range(len(s)):
            _chr = s[ind]
            if _chr == " " :
                pass
            
            elif _chr == "(" :
                mult.append(1) if  add else mult.append(-1)
                ans.append(0)
                num = ["0"]
                add = True
                
                                
            elif _chr == "+" or _chr == "-" or _chr == ")":
                if add:
                    ans[-1] += int("".join(num))
                else: ans[-1] -= int("".join(num))
                num = ["0"]
                
                if _chr == ")":
                    ans[-2] += (ans[-1]* mult[-1])
                    mult.pop()
                    ans.pop()
                else:
                    add = True if _chr == "+" else False
    
            else:
                num.append(_chr)
                   
        if add:
            ans[-1] += int("".join(num))
        else: ans[-1] -= int("".join(num))

        return ans[-1]
            