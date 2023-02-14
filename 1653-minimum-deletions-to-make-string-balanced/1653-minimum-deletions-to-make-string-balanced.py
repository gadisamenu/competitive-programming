class Solution:
    def minimumDeletions(self, s: str) -> int:
        left_bs = []
        right_as = deque()
        count = 0
        for i in range(len(s)):
            left_bs.append(count)
            if s[i] == "b":
                count += 1
            
            
        count = 0
        for i in range(len(s)-1,-1,-1):
            right_as.appendleft(count)
            if s[i] == "a":
                count += 1
                
        i = 0
        j = len(s)-1
        removed_a = 0
        removed_b = 0
        
        while i < j:
            while i < j and s[i] == "a":
                i += 1
            while j > i and s[j] == "b":
                j -= 1
            if i < j:
                if s[i] == "b":
                    if s[j] == "a":
                        if right_as[i] - removed_a > left_bs[j] - removed_b:
                            i += 1
                            removed_b += 1
                        else:
                            removed_a +=1
                            j -= 1
                            
                    else:
                        removed_a +=1
                        j -= 1
                else:
                    removed_a += 1
                    j -= 1
      
        
        return removed_a + removed_b
        
    