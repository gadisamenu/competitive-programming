class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        count = Counter(candidates)
                        
        keys = list(count.keys())
        path = []
        answer = set()
                        
    
        def backtracking(index,target):
            if target == 0:
                answer.add(tuple(path))
                return
             
            if index < len(keys) and  target > 0:
                backtracking(index+1,target)
                
                count[keys[index]] -= 1
                
                target -= keys[index]
                path.append(keys[index])
                
                if count[keys[index]] > 0:
                    backtracking(index,target)
                
                backtracking(index+1,target)
                
                count[keys[index]] += 1
                
                path.pop()
                
        
        backtracking(0,target)
        
        return answer
        
        
 
        