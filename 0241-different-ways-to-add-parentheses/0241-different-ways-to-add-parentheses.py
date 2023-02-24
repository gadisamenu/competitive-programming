class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        oper = {"+":operator.add,"-":operator.sub,"*":operator.mul}
        
        def recursion(left, right):
            ans = []
            for i in range(left, right):
                if expression[i] in oper:
                    left_val = recursion(left,i)
                    right_val = recursion(i+1,right)
                    for lft in left_val:
                        for rgt in right_val:
                            ans.append(oper[expression[i]](lft,rgt))
                            
            return ans if len(ans) != 0 else [int(expression[left:right])]
  
        return recursion(0, len(expression))
                
                
            