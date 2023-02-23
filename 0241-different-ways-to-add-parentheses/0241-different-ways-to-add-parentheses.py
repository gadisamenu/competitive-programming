class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        oper = {"+":operator.add,"-":operator.sub,"*":operator.mul}
        
        def recursion(left, right):
            ans = []
            for i in range(left, right):
                if expression[i] not in oper:
                    continue
                ans += [oper[expression[i]](lft, rgt) for lft in recursion(left, i)
                                            for rgt in recursion(i + 1, right)]
                
            return ans if len(ans) != 0 else [int(expression[left:right])]
  
        return recursion(0, len(expression))
                
                
            