class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        left = deque()
        m = -1
        for i in range(len(dominoes)-1,-1,-1):
            if dominoes[i] == "L": m = i
            elif dominoes[i] == "R": m = -1
            left.appendleft(m)
            
       
        ans = []
        right = -1
        for i  in range(len(dominoes)):
            if dominoes[i] =="L": right= -1
            elif dominoes[i] =="R": right = i
                
            if left[i] != -1 and right == -1: ans.append('L')
            elif right ==  -1 and left[i] == -1: ans.append(".")
            elif right != -1 and left[i] == -1: ans.append("R")
            else:
                if i - right== left[i] -i :ans.append(".")
                elif i -right < left[i] -i: ans.append("R")
                else:ans.append("L")
                    
        return "".join(ans)
            
                
            
            
            
            
            