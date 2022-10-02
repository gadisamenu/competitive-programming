class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        like_time = 0
        _sum = 0
        
                
        for i in range(len(satisfaction)):
            _sum += satisfaction[i]
            if like_time  +  _sum  >= like_time:
                like_time += _sum
            else:break
                
        return like_time
            