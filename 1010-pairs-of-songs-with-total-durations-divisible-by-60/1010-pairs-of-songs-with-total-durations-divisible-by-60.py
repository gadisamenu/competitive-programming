class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        remander = defaultdict(int)
        
        for t in time:
            remander[t%60]+=1
        
        answer = 0
        for rem in remander.keys():
            op = 60-rem
            if rem == op or rem == 0:
                answer += (remander[rem]*(remander[rem]-1))//2
                remander[rem]= 0
            elif op in remander:
                answer += remander[rem]*remander[op]
                remander[rem]= 0
            
        return answer
        
        
        