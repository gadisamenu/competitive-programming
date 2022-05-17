class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        ones = bin(n)
        if ones[0] == "-":
            return False
        seen = False
        for n in ones:
            if  n == "1":
                if seen:return False
                seen = True
        return True if seen else False