class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = defaultdict(int)
        longest = 0
        maxim = deque()
        jump = False
        i =0 
        j =0
        while j< len(s):
            
            if not jump:
                jump = False
                counts[s[j]]+=1
                while maxim and counts[maxim[-1]] <= counts[s[j]]:
                    maxim.pop()
                maxim.append(s[j])
            if j-i+1- counts[maxim[0]] > k:
                counts[s[i]]-=1
                if maxim[0]== s[i]:
                    maxim.popleft()
                    while maxim and counts[maxim[-1]] < counts[s[i]]:
                        maxim.pop()
                    maxim.append(s[i])
                jump = True
                i+=1
                
            else:
                jump=False
                longest = j-i+1 if longest < (j-i+1) else longest
                j+=1
                
        return longest
    
    
