class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:    
        answer = 0
        stack = []
        
        for i in range(len(heights)):
            
            while stack and heights[i] < heights[stack[-1]]:
                popped = stack.pop()
                width = i
                if stack: width -= (stack[-1] + 1)
                answer = max(answer,heights[popped] * width)
            

            stack.append(i)  
            
            
        while stack:
            index = stack.pop()
            width = len(heights)
            if stack:
                width -= (stack[-1] + 1)

            answer = max(answer,width * heights[index])

            
        return answer


        