class Solution:
    def numSplits(self, s: str) -> int:
        left_count = defaultdict(int)
        right_count = Counter(s)
        good_splits = 0
        for i in range(0,len(s)-1):
            left_count[s[i]] += 1
            right_count[s[i]] -= 1
            if not right_count[s[i]]:
                right_count.pop(s[i])
            if len(right_count) == len(left_count):
                good_splits += 1
                
        return good_splits