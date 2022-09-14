class Solution:
    def countCollisions(self, directions: str) -> int:
        pre = directions[0]
        col = 0
        keep = 0  if pre != "R" else -1
        for d in directions:
            if pre == "R":
                if  d == "L":
                    col += 2 + keep
                    keep = 0
                    pre = "S"
                elif d == "S":
                    col += 1 + keep 
                    keep = 0
                    pre = "S"
                else:
                    keep += 1
            elif pre == "S" and d == "L":
                col += 1
                
            else: pre = d
                
        return col