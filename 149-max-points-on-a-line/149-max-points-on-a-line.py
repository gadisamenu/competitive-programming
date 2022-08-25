class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        lgth  = len(points)
        ans = 0
        count =defaultdict(lambda:defaultdict(int))
        
        for i in range(lgth):
            n = (points[i][0],points[i][1])
            for j in range(lgth):
                if i != j:
                    denom = n[1] - points[j][1]
                    if denom:
                        slp = (n[0]-points[j][0])/denom
                    else:
                        slp = "v"
                    count[slp][n]+= 1
                    ans = max(count[slp][n],ans)
        return ans+1