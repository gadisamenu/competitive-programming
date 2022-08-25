class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(magazine)
        n_count = defaultdict(int)
        for n in ransomNote:
            if n_count[n] == count[n]:
                return False
            n_count[n]+=1
            
        return True