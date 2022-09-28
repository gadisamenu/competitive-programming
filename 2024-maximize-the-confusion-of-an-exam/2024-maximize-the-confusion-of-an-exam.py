class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        i = 0
        j = 0
        count = {"T":0,"F":0}
        count[answerKey[0]] += 1
        _max = 1
        while j < len(answerKey):
            while min(count["T"],count["F"]) > k:
                count[answerKey[i]] -= 1
                i += 1
            _max = max(j -i+1,_max)
            j += 1
            if j < len(answerKey):count[answerKey[j]] += 1

        return _max
            
            