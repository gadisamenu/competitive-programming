class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        mapped = set()
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]:
                    return False
            elif t[i] not in mapped:
                mapped.add(t[i])
                mapping[s[i]] = t[i]
            else:
                return False
        
        return True
                    