class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        
        _dp = [int(matrix[-1][i]) for i in range(cols)]
        _dp.append(0)
        _cur = [0 for i in range(cols+1)]
        
        answer = max(_dp)
        for r in range(rows-2,-1,-1):
            for c in range(cols-1,-1,-1):
                if matrix[r][c] == "1":
                    _cur[c] = 1+min(_dp[c],_dp[c+1],_cur[c+1])
                    answer = max(answer,_cur[c])
                else:
                    _cur[c] = 0
            temp = _dp
            _dp = _cur
            _cur = temp
            
        return answer**2   
    