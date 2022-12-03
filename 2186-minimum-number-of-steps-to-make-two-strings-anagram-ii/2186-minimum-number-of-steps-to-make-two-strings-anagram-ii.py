class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)
        letters = set(count_s)
        letters.update(count_t)
        
        answer = 0
        for ltr in letters:
            answer += abs(count_s[ltr]-count_t[ltr])
        return answer