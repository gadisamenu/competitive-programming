class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count = {5:0,10:0}
        
        for bill in bills:
            if bill == 5:
                count[bill] += 1
            elif bill == 10:
                if count[5] > 0: 
                    count[5] -= 1
                    count[10] += 1
                else: return False
            else:
                if count[10] > 0:
                    count[10] -= 1
                    if count[5] > 0: count[5] -= 1
                    else:return False
                elif count[5] >2: count[5] -= 3
                else: return False
        return True
            
            