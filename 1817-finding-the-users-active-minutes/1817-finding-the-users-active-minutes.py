class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        answer = [0 for _ in range(k)]
        
        UAM = defaultdict(set)
        
        for log in logs:
            UAM[log[0]].add(log[1])
            
        for user in UAM:
            if len(UAM[user]) <= k:
                answer[len(UAM[user])-1] += 1
                
        return answer