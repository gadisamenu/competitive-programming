class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        
        lgth = len(nums)
        
        dp = [[1,1] for _ in range(lgth)]
        
        for current in range(lgth):
            for prev in range(current-1,-1,-1):
                if nums[current] > nums[prev]:
                    sub_sqnc_lgth = dp[prev][0] + 1
                    if sub_sqnc_lgth  > dp[current][0]:
                        dp[current][0] = sub_sqnc_lgth
                        dp[current][1] = dp[prev][1]
                    elif sub_sqnc_lgth == dp[current][0]:
                        dp[current][1] += dp[prev][1]
    
                        
        answer = 0
        _max = 0
        for i in range(lgth):
            if dp[i][0] > _max:
                _max = dp[i][0]
                answer = dp[i][1]
            elif dp[i][0] == _max:
                answer += dp[i][1]
                
        return answer
            
        
    