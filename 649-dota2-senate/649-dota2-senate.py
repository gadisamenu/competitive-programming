class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senate = list(senate)
        lgth = len(senate)
        ranges = lgth-1
        last=senate[0]
        i = 0
        killed_d= killed_r = 0
        while ranges:
            if senate[i] == "R":
                if killed_r:
                    senate[i]="F"
                    killed_r-=1
                else:
                    last ="D"
                    killed_d+=1
                    ranges-=1
            elif senate[i] == "D":
                if killed_d:
                    senate[i]= "F"
                    killed_d -=1
                else:
                    last="D"
                    killed_r+=1
                    ranges -= 1
            i = (i+1)%lgth
            
        if killed_r < killed_d:
            return "Radiant"
        elif killed_r == killed_d:
            return "Radiant" if last == "R" else "Dire"
        else:
            return "Dire"
            
            
            
                
            
    