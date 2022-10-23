class Solution:
    def minOperations(self, n: int) -> int:
        _sum = (n + n *(n-1))
        return _sum // 4
            