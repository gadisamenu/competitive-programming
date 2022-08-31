class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        row = len(matrix)
        col = len(matrix[0])
        visited = set()
        @cache
        def dp(rw,cl):
            ans =  0
            if rw +1 < row and matrix[rw][cl] > matrix[rw+1][cl]:
                ans = max(ans,dp(rw + 1,cl))
                visited.add((rw+1,cl))
            if rw - 1 > -1 and matrix[rw][cl] > matrix[rw-1][cl]:
                visited.add((rw -1,cl))
                ans = max(ans,dp(rw - 1,cl))
            if cl + 1 < col and matrix[rw][cl] > matrix[rw][cl+ 1]:
                visited.add((rw,cl + 1))
                ans = max(ans,dp(rw,cl + 1))
            if cl - 1 > -1 and matrix[rw][cl] > matrix[rw][cl - 1]:
                visited.add((rw,cl- 1))
                ans = max(ans,dp(rw, cl -1))
            return ans + 1
        
        ans = 0
        for n in range(row):
            for m in range(col):
                if matrix[n][m] not in visited:
                    visited.add((n,m))
                    ans =max(ans,dp(n,m))
        return ans