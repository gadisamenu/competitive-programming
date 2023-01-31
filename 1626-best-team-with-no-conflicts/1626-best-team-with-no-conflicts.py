class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        for i in range(len(ages)):
            ages[i]  = [ages[i],scores[i]]
            
        ages.sort()
        
        for i in range(len(ages)-1,-1,-1):
            _max_left = 0
            j = i + 1
            while j < len(ages):
                if ages[i][1] <= ages[j][1]:
                    _max_left = max(_max_left,ages[j][0])
                j += 1
            if j < len(ages):
                _max_left = ages[j][0]
            ages[i][0] = ages[i][1] + _max_left
        return max(ages,key=lambda x: x[0])[0]
                
                
            
    