class Solution:
    def maxJump(self, stones: List[int]) -> int:
        answer = stones[1] -stones[0]
        i = 0
        j = 2
        while j < len(stones):
            diff = stones[j] - stones[i]
            if answer < diff:
                answer = diff
            i += 1
            j += 1
            
        return answer
        