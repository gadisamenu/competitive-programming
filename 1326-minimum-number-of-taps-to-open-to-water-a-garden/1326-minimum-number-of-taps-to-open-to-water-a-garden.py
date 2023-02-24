class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        for i in range(len(ranges)):
            ranges[i] = [i-ranges[i],i+ranges[i]]
            
        ranges.sort()
        start = 0
        end = 0
        taps = 1
        for i in range(len(ranges)):            
            if start < ranges[i][0]:
                if end >= ranges[i][0]:
                    if end < ranges[i][1]:
                        print(start,end)
                        taps += 1
                        start = end
                        end = ranges[i][1]
                else:
                    return -1
            elif end < ranges[i][1]:
                end = ranges[i][1]
            
            if end >= n:
                return taps
         
        return -1
                


        