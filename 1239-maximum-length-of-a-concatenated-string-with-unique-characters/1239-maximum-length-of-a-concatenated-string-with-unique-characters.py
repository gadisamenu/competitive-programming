class Solution:
    def maxLength(self, arr: List[str]) -> int:
        index = {}
        for i in range(26):
            index[chr(i+97)] = i
            
        @cache
        def dp(i,letters):
            if i >= len(arr):
                return 0
            old = letters
            valid = True
            for ltr in arr[i]:
                if letters & 1<<index[ltr]:
                    valid = False
                    break
                letters |= 1 << index[ltr]
            if valid:
                return max(len(arr[i]) + dp(i+1,letters),dp(i+1,old))
            return dp(i+1,old)
        
        return dp(0,0)
            