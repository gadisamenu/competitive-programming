class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = {"B":0,"W":0}
        for  i in range(k):
            count[blocks[i]] += 1
            
        left = 0  
        answer = count["W"]
        for right in range(k,len(blocks)):
            count[blocks[right]] += 1
            count[blocks[left]] -= 1
            left += 1
            answer = min(answer,count["W"])
        
        return answer
        
            
        
        