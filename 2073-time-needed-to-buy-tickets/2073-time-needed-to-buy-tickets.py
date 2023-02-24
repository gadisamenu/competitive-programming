class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        
        answer = tickets[k]
        for i in range(k):
            answer += min(tickets[k],tickets[i])
            
        tickets[k] -= 1
        for i in range(k+1,len(tickets)):
            answer += min(tickets[k],tickets[i])
            
        return answer