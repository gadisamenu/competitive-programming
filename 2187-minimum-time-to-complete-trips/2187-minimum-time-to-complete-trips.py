class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        
        start = 0
        end = totalTrips*max(time)
        
        t_ans= 0
        while start <= end:
            
            mdl = start + (end-start)//2
            
            trips = 0
            
            for t in time:
                trips += (mdl//t)
                
                
            if trips < totalTrips:
                start = mdl + 1
            else:
                t_ans = mdl
                end = mdl-1
                
                
        return t_ans
        