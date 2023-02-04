class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        def compr(cnt):
            for ltr in count_s1:
                if cnt[ltr] != count_s1[ltr]:
                    return False
            return True
        
        w_count = defaultdict(int)
        for i in range(len(s1)-1):
            w_count[s2[i]] += 1
        
        count_s1= Counter(s1)
        i = 0
        j = len(s1)- 1
        while j < len(s2):
            w_count[s2[j]] += 1
            if compr(w_count):
                return True
            w_count[s2[i]] -= 1
            j += 1
            i += 1
            
        return False
            
        
        