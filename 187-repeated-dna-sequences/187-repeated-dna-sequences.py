class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        lgth = len(s)+1
        occurance = defaultdict(int)
        i = 0 
        j = 10
        while j < lgth:
            occurance[s[i:j]]+=1
            i+=1
            j+=1
        for substr in list(occurance):
            if occurance[substr]==1:
                occurance.pop(substr)
        return occurance
                