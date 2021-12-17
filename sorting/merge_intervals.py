class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        list_m = []
        
        intervals.sort(key=lambda x:x[0])
        
        for interval in intervals:
            # if empty or no interval then simply append
            if not list_m or list_m[-1][1] < interval[0]:
                list_m.append(interval)
            else: # it overlap exist, then update the latest end
                list_m[-1][1] = max(list_m[-1][1], interval[1])
        
