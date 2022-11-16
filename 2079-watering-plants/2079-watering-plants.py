class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        
        water = capacity
        steps  = 0
        for i in range(len(plants)):
            if water < plants[i]:
                water = capacity
                steps += i*2
            steps += 1
            water -= plants[i]
            
        return steps
    
    