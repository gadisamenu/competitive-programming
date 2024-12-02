class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])
        time = 0
        heap = []
        
        for dur,due in courses:
            if dur + time <= due:
                heappush(heap,(-dur,due))
                time += dur
            elif heap and -heap[0][0] > dur:
                old_dur,_ = heapreplace(heap,(-dur,due))
                time += (old_dur + dur)
                
        return len(heap)
                    