class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        _max = neededTime[0]
        pre = colors[0]
        took = 0
        for i in range(1,len(colors)):
            if pre == colors[i]: _max = max(neededTime[i],_max)
                
            else:
                took += _max
                _max= neededTime[i]
                pre = colors[i]
                
        took += _max
        return sum(neededTime) -took
    
    
            
                