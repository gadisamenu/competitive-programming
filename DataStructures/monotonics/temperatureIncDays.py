class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        nexts =[0]
        kickers ={}
        ans=[0]*len(temperatures)
        for ind in range(len(temperatures)):
            while nexts:
                if temperatures[nexts[-1]] < temperatures[ind] :
                    ans[nexts[-1]] = abs(nexts[-1] - ind)
                    nexts.pop()
                    if not nexts or nexts[-1] == ind:
                        nexts.append(ind)
                        break
                else:
                    nexts.append(ind)
                    break
        return ans