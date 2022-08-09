class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        indexs = {}
        
        for ind,num in enumerate(arr):
            indexs[num] = ind

        @cache
        def dp(ind):
            ans = 1
            for i in range(ind-1,-1,-1):
                if (arr[ind] % arr[i]) == 0:
                    num = arr[ind] // arr[i]
                    if num in indexs:
                        ans += (dp(i) * dp(indexs[num]))
                        
            return pow(ans,1,1000000007)

        ans = 0
        for n in range(len(arr)):
            ans += dp(n)
            
        return pow(ans,1,1000000007)
            
        
        