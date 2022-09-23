class Solution:
    def maximumRows(self, matrix: List[List[int]], numSelect: int) -> int:
        self.ans = 0
        col = len(matrix[0])
        path = set()
        def backtracking(c):
            if len(path) == numSelect:
                count = 0
                for r in matrix:
                    for i in range(len(r)):
                        if i not in path and r[i]:
                            count += 1
                            break
                self.ans = max(self.ans,len(matrix)-count)
            elif c < col:
                backtracking(c+1)
                path.add(c)
                backtracking(c+1)
                path.remove(c)
        
        backtracking(0)
        return self.ans
    
                
                    