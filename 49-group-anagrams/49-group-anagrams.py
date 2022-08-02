class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        groups = defaultdict(list)
        for _str in strs:
            count = tuple(sorted(_str))
            groups[count].append(_str)

        return groups.values()
            
            