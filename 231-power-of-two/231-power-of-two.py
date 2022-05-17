class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 0:
            return False
        ones = bin(n).count("1")
        return True if ones == 1 else False