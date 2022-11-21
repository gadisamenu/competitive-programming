class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
               
        for i in range(len(gas)):
            gas[i] -= cost[i]
        
        for i in range(1,len(gas)):
            gas[i] += gas[i-1]
            
        if gas[-1] <0:
            return -1
        
        _min = 0
        for i in range(len(gas)):
            if gas[_min] >= gas[i]:
                _min = i
        
        return (_min+1) %len(gas)
                
            