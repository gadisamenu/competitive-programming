class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) %2 == 1 :return []
        changed.sort()
        doubles = defaultdict(list)
        ans = []
        for n in changed:
            if doubles[n]:
                ans.append(doubles[n].pop())
                if not doubles[n]: doubles.pop(n) 
            else:
                doubles.pop(n) 
                doubles[n*2].append(n)
        return ans if not doubles else []