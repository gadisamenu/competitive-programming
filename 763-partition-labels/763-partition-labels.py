class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counts = Counter(s)     
        still = set()
        ans =[]
        i = 0
        j= 0
        while j < len(s):                
            if counts[s[j]] == 1:
                counts.pop(s[j])
                if s[j] in still: still.remove(s[j])
                if not still:
                    ans.append(j-i+1)
                    i = j+1
            else: 
                counts[s[j]]-=1
                if s[j] not in still:still.add(s[j])
            j+=1            
        return ans
            
                
            