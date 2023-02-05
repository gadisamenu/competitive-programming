class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s) < len(p):
            return []
        
        count = Counter(p)
        for i in range(len(p)-1):
            if count[s[i]] == 1:
                count.pop(s[i])
            else:
                count[s[i]] -= 1
         
        answer  = []
        i = 0
        j = len(p)-1
        
        while j < len(s):
            if count[s[j]] == 1:
                count.pop(s[j])
            else:
                count[s[j]] -= 1
            if not len(count):
                answer.append(i)
                
            if count[s[i]] == -1:
                count.pop(s[i])
            else:
                count[s[i]] += 1
            i += 1
            j += 1
        return answer
        
            
        
            