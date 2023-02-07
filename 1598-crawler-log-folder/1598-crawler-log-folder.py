class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        
        for log in logs:
            log = log[:-1]
            if log == "..":
                if stack:
                    stack.pop()
            elif log != ".":
                stack.append(log)
        return len(stack)