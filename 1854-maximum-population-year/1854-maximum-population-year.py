class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        _math = defaultdict(int)
        
        for log in logs:
            _math[log[0]] += 1
            _math[log[1]] -= 1
        
        keys = sorted(_math)
        
        populations = 0
        answer = 0 
        _max_pop = 0
        for key in keys:
            populations += _math[key]
            if populations > _max_pop:
                _max_pop = populations
                answer = key
        return answer
            