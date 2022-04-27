class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        lgth = len(arr)//2
        occurence = Counter(arr)
        sorted_nums = sorted(occurence, key = lambda x: -occurence[x])
        ans = 0
        _sum = 0
        for num in sorted_nums:
            if _sum < lgth:
                _sum+=occurence[num]
                ans +=1
            else:
                break
        return ans