class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if targetCapacity > jug1Capacity + jug2Capacity: return False
        while True:
            if jug2Capacity == 0:
                break
            k = jug1Capacity
            jug1Capacity = jug2Capacity
            jug2Capacity = k %jug2Capacity
            
        return  False if targetCapacity %  jug1Capacity  else True
        
                