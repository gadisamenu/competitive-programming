class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for idx in range(len(num)):
            if not k:
                stack.extend(num[idx:])
                break
            while stack and k and int(stack[-1]) > int(num[idx]):
                k -= 1
                stack.pop()
                
            if  not (num[idx] == '0' and not stack):
                stack.append(num[idx])
                
        while k and stack:
            k -= 1
            stack.pop()
        
        for n in range(len(stack)):
            if  stack[n] != '0':
                stack = stack[n:]
                break
        
        return "".join(stack) if stack else "0"
                
    
