"""
   This is the custom function interface.
   You should not implement it, or speculate about its implementation
   class CustomFunction:
       # Returns f(x, y) for any given positive integers x and y.
       # Note that f(x, y) is increasing with respect to both x and y.
       # i.e. f(x, y) < f(x + 1, y), f(x, y) < f(x, y + 1)
       def f(self, x, y):
  
"""

class Solution:
    def findSolution(self, customfunction: 'CustomFunction', z: int) -> List[List[int]]:
        
        solutions = []
       
        for let_x in range(1,1000+1):
            y_min = 1 
            y_max= 1000
            while y_min <= y_max:
                let_y = y_min + (y_max- y_min)//2
                
                out_put= customfunction.f(let_x,let_y)
                
                if out_put == z:
                    solutions.append([let_x,let_y])
                    break
                elif out_put < z:
                    y_min = let_y +1
                else:
                    y_max = let_y -1
        return solutions
