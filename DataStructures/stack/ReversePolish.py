# import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        oper = ['*','+','-' , '/']
        values = []
        for mem in tokens:
            if mem in oper:
                if values:
                    frst = values.pop()
                    scnd = values.pop()
                    if mem =="/":
                        values.append(int(scnd / frst))
                    elif mem =="*":
                        values.append(scnd * frst)
                    elif mem =="-":
                        values.append(scnd - (frst))
                    elif mem =="+":
                        values.append(scnd + frst)
            else:
                
                values.append(int(mem))
        return values.pop()
        