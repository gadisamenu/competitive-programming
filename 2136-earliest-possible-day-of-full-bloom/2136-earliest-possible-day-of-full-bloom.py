class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        for i in range(len(plantTime)):
            plantTime[i]= [growTime[i],plantTime[i]]
            
        
        plantTime.sort(reverse=True)
        days = 0
        grow_time = 0
        for i in range(len(plantTime)):
            days += plantTime[i][1]
            grow_time = max(grow_time-plantTime[i][1],plantTime[i][0])
            
        return days + grow_time