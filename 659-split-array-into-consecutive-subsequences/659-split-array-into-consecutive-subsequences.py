class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        series_end = Counter()
        available = Counter(nums)
        
        for i in range(len(nums)):
            no = nums[i]
            if not available[no]: 
                continue
            available[no] -= 1
            if series_end[no - 1]: 
                series_end[no] += 1
                series_end[no - 1] -= 1
            elif available[no + 1] and available[no + 2]:
                available[no + 1] -= 1
                available[no + 2] -= 1
                series_end[no + 2] += 1
            else:
                return False
        return True