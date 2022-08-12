class Solution:
    def numberToWords(self, num: int) -> str:
        numbers =           {0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:'Thirteen',14:"Fourteen",15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100:"Hundred",1000:"Thousand",1000000:"Million",1000000000:"Billion"}
        
        if num == 0: return numbers[0]
        
        def recursion(num,divider):
            
            ans = []
            cur_num = num //divider
            
            quotient = cur_num // 100
            if quotient != 0:
                ans.append(numbers[quotient])
                ans.append(numbers[100])
            cur_num %= 100
                                
            if cur_num  < 20:
                 if cur_num != 0:
                    ans.append(numbers[cur_num])
            
            else:
                quotient = cur_num // 10
                if quotient != 0:
                    ans.append(numbers[quotient*10])
                cur_num %= 10
                
                if cur_num != 0:
                    ans.append(numbers[cur_num])
                    
            if divider == 1: return ans
            if ans:
                ans.append(numbers[divider])
                
            
            ans.extend(recursion(num%divider,divider//1000))
            return ans
        
        return " ".join(recursion(num,1000000000))