class Solution:
    def sumZero(self, n: int) -> List[int]:
        answer = []
        number = 1
        _sum = 0
        if n == 1:
            return [0]
        odd = False
        if n %2 == 1:
            odd = True
            n -= 3
        
        while len(answer) < n:
            if _sum:
                answer.append(_sum)
                _sum = 0
            else:
                _sum = -number
                answer.append(number)
                number += 1
        if odd:
            answer.append(number)
            answer.append(number+1)
            answer.append(number*-2-1)
        return answer
           
    