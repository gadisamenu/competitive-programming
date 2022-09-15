class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        arr.sort()
        doubles = defaultdict(int)
        for n in arr:
            if doubles[n]:
                doubles[n] -= 1
                if not doubles[n]: doubles.pop(n)
            else:
                doubles.pop(n)
                if n < 0:
                    doubles[n/2] += 1
                else:
                    doubles[2*n] += 1
        return False if doubles else True