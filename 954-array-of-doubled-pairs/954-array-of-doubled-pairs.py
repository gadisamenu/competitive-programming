class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        doubles = defaultdict(list)
        for n in arr:
            if doubles[n]:
                doubles[n].pop()
                if not doubles[n]: doubles.pop(n)
            else:
                doubles.pop(n)
                if n < 0:
                    doubles[n/2].append(n)
                else:
                    doubles[2*n].append(n)
                
        return False if doubles else True