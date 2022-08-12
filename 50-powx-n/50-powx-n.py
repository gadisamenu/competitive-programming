class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1/x
        val = self.myPow(x,n//2)
        odd =  x if n%2 else 1
        return val * val * odd