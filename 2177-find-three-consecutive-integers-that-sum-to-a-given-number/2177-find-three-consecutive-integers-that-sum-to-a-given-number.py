class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if not num%3:
            n = num//3
            return [n-1,n,n+1]
        return []