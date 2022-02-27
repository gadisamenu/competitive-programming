class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        # self.persons = persons
        self.times =times
        self.winners = self.ranker(persons)
        
    def ranker(self,persons):
        votes = {persons[0]:1}
        j = 1
        winners =[persons[0]]
        while j < len(persons):
            if persons[j] in votes:
                votes[persons[j]]+=1
            else:
                votes[persons[j]] = 1

            if votes[winners[-1]] == votes[persons[j]]:
                    winners.append(persons[j])
            elif votes[winners[-1]] > votes[persons[j]]:
                winners.append(winners[-1])
            else:
                winners.append(persons[j])
            j+=1
        return winners
       
    
    def q(self, t: int) -> int:
        left = 0
        right = len(self.times)-1
        
        while left <= right:
            m = left  + (right-left)//2
            
            if t < self.times[m]:
                right = m-1
                
            elif t > self.times[m]:
                left  = m+1
            else:
                return self.winners[m]
        if self.times[m] > t:
            return self.winners[m-1]
        return self.winners[m]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)