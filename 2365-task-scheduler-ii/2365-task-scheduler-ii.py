class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        last_time = defaultdict(int)
        days = 0
        for task in tasks:
            days += 1
            if last_time[task]:
                gap =days- last_time[task]-1
                if gap < space:
                    days += space -gap
            
            last_time[task] = days
            
        return days