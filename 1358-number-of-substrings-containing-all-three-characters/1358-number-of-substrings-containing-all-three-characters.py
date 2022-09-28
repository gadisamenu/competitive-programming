class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = defaultdict(int)
        i = 0
        j = -1
        ans =0
        while j < len(s):
            if len(count) < 3:
                j+=1
                if j < len(s): count[s[j]] +=1
            else:
                ans += len(s) -j
                if count[s[i]] == 1:count.pop(s[i])
                else:count[s[i]] -= 1
                i+= 1
        return ans
                    
        