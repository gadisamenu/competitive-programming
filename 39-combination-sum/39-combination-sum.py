class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        self.ans = set()

        def dp(ind:int, target:int)->list:
            if target < 0 or ind == len(candidates):
                return
            if target== 0:
                self.ans.add(tuple(path))
            else:   
                dp(ind + 1,target)
                path.append(candidates[ind])
                dp(ind + 1, target - candidates[ind])            
                dp(ind,target- candidates[ind])
                path.pop()
  
        dp(0,target)
        return self.ans
    
        
                
                
            
                
            
                
            
            