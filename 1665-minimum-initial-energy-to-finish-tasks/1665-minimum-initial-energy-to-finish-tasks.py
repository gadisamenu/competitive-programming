class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        tasks.sort(key=lambda x:(x[0] - x[1],x[0]))
     
        answer = 0
        energy = 0
        for task in tasks:
            if energy < task[1]:
                answer += task[1] - energy
                energy = task[1]
            energy -= task[0]
            
        return answer
