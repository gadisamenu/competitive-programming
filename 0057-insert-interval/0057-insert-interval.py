class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        answer = []
        index = 0
        while index < len(intervals):
            if intervals[index][1] >= newInterval[0]:
                break
            answer.append(intervals[index])
            index += 1
      

        if index < len(intervals):
            if index == 0 and newInterval[1] < intervals[0][0]:
                answer.append(newInterval)
            else:
                start= min(intervals[index][0],newInterval[0])
                while index < len(intervals):
                    if newInterval[1] < intervals[index][0]:
                        break
                    index += 1
                end = max(intervals[index-1][1],newInterval[1])
                answer.append([start,end])
            
            for i in range(index,len(intervals)):
                answer.append(intervals[i])
            
        else:
            answer.append(newInterval)
        return answer

