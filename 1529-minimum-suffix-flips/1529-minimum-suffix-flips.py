class Solution:
    def minFlips(self, target: str) -> int:
        ans = 0
        pre = "0"
        for n in target:
            if n!= pre:
                pre = n
                ans += 1
        return ans