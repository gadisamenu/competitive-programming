class Solution:
    def frequencySort(self, s: str) -> str:
        count = Counter(s)
        
        sorted_freq =sorted(count, key = lambda x: -count[x])
        answer = []
        for letter in sorted_freq:
            answer.append(letter*count[letter])
        return "".join(answer)
    