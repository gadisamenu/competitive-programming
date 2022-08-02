class Solution:
    def intToRoman(self, num: int) -> str:
        ans = []
        dividers  = {1000:"M",500:"D",100:"C",50:"L",10:"X",5:"V",1:"I"}

        for n in dividers:
            
            if 900 <= num < 1000:
                ans.append("CM")
                num -= 900
                
            elif 400 <= num < 500:
                ans.append("CD")
                num -= 400
                
            elif 90 <= num < 100:
                ans.append("XC")
                num -= 90
                
            elif 40 <= num < 50:
                ans.append("XL")
                num -= 40
                
            elif 9  == num:
                ans.append("IX")
                num -= 9
                
            elif num == 4:
                ans.append("IV")
                num -= 4
           
            elif num >=  n:
                ans.append(dividers[n] * (num//n))
                num  %= n

            
        return "".join(ans)
                

                
                