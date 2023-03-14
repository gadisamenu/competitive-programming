class Solution:
    def nextGreaterElement(self, n: int) -> int:
        stack = deque()
        
        while n:
            digit = n%10
            n //= 10
            if stack and digit < stack[-1]:
                break
            stack.append(digit)
            
        index = 0
        for i in range(len(stack)-1,-1,-1):
            if digit >= stack[i]:
                break
            index = i

        if digit >= stack[index]:
            return -1
        
        stack.appendleft(stack[index])
        stack[index+1] = digit
        
        for i in range(len(stack)):
            n *= 10
            n += stack.popleft()

        return n if n <= 2147483647 else -1
    
    
