class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        answer = 0
        for word in words:
            prefix = True
            for i in range(len(pref)):
                if i >= len(word) or pref[i] != word[i]:
                    prefix = False
                    break
            if prefix:
                answer += 1
        return answer