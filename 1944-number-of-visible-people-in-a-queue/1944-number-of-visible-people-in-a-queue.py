class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        """ binary search for next greater element in stack"""
        def binary_src_rv(_list,tr):
            l = 0
            r = len(_list)-1
            while l <= r:
                m = l + (r-l)//2
                
                if _list[m]  > tr:
                    l = m +1
                elif _list[m] < tr:
                    r = m- 1
                else:return m
            return m
        lgth = len(heights)
        stack = []
        
        n_grt = [lgth for _ in range(lgth)]
        for i in range(lgth):
            while stack and heights[stack[-1]]  < heights[i]:
                n_grt[stack.pop()]= i
            stack.append(i)
            
   
        stack=[heights[-1]]
        ans = deque([0])
        for i in range(2,lgth+1):
            
            m = len(stack)
            if n_grt[-i] != lgth:
                m -=  binary_src_rv(stack,heights[n_grt[-i]])
            
            ans.appendleft(m)
            while stack and stack[-1] < heights[-i]:
                stack.pop()
            stack.append(heights[-i])
            
        return ans
            
            