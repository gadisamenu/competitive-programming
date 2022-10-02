from sortedcontainers import SortedList

class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand)%groupSize: return False
        
        count  = Counter(hand)
        sorted_l = SortedList(count.keys())
        num_groups = len(hand)//groupSize
        
        
        while num_groups:
            mov = 0
            for i in range(groupSize):
                if i  == groupSize-1 or (len(sorted_l) > i+1+mov and sorted_l[i+1+mov] - sorted_l[i+mov] == 1):
                    
                    if count[sorted_l[i+mov]] == 1:
                        sorted_l.pop(i+mov)
                        mov -= 1
                        
                    else: count[sorted_l[i+mov]] -=1
                        
                else: return False
                    
            num_groups -= 1
            
        return True
        
        

            
            