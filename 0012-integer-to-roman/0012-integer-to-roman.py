class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        dividers  = {1000:"M",900:"CM",500:"D",400:"CD",100:"C",90:"XC",50:"L",40:"XL",10:"X",9:"IX",5:"V",4:"IV",1:"I"}

        for n in dividers:
            if num >=  n:
                ans.append(dividers[n] * (num//n))
                num  %= n

            
        return "".join(ans)
                

                
                