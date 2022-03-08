class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = defaultdict(int)
        
        for char in s:
            count[char]+=1
        
        m = 0
        ans = 0
        for c in count:
            if count[c]%2 == 0:
                ans += count[c]
            else:
                m+=1
                ans+=count[c]-1
        return ans +1 if m else ans
            
            