class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer = defaultdict(list)
        
        for word in strs:
            answer[str(sorted(word))].append(word)
            
        return answer.values()