class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        numbers = [1,1]
        
        while True:
            _sum = numbers[-1] + numbers[-2]
            if _sum <= k:
                numbers.append(_sum)
            else:break
     
        i = len(numbers)-1
        count = 0
        while k:
            diff = k -numbers[i]
         
            if diff >= 0:
                k -= numbers[i]
                count += 1
            i -= 1
        return count
            