class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        _min = float("inf")
        
        timePoints.sort()
        pre = None
                
        for time in timePoints:
            hour,minute = tuple(map(int,time.split(":")))
            if pre:
                _min = min(_min,(hour-pre[0])*60 + minute-pre[1])
            pre = (hour,minute)
        
        n_hour,n_minute = tuple(map(int,timePoints[0].split(":")))
        
        return min(_min,(n_hour-hour+24)*60 + n_minute-minute)
        