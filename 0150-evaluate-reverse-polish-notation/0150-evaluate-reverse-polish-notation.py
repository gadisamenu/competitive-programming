class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {"+","-","*","/"}
        for token in tokens:
            if token in operations:
                scnd = stack.pop()
                frst = stack.pop()
                value = eval("int(" + frst + token + scnd + ")")
                stack.append(str(value))
               
            else:
                stack.append(token)
               
            
        return int(stack[-1])