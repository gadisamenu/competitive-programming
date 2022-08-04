class Solution:
    def minWindow(self, s: str, t: str) -> str:
        count = defaultdict(int)
        count_t  = Counter(t)
        
        t = set(t)
        ans  = [0,float('inf')]
        
        do = True
        good = 0
        i,j = 0, 0
        
        while i<=j and j < len(s):
            
            if do:
                count[s[j]] += 1
            
                if count[s[j]]  == count_t[s[j]]:
                    good += 1

            if good == len(t):
                if count[s[i]] == count_t[s[i]]:
                    good -= 1
            
                if ans[1]  >  j - i + 1 : 
                    ans[0] = i 
                    ans[1] = j-i + 1
                                        
                count[s[i]] -= 1
                i += 1
                do =False
                
            else:
                j+=1 
                do = True

                
        if ans[1] == float('inf'):
            return ""
        return s[ans[0]:ans[0]+ans[1]]
                
            
            
            
            
            
            