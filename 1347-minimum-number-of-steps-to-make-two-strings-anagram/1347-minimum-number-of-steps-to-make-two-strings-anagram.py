class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        answer = 0
        for k in count_s:
            if count_s[k] > count_t[k]:
                answer += count_s[k]-count_t[k]
                
        return answer
            