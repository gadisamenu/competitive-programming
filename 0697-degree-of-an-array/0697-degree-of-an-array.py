class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        count = Counter(nums)
        frequent = max(count,key = lambda x: count[x])
        degree = count[frequent]
        if degree == 1:
            return 1
        answer = float("inf")
        count = defaultdict(int)
        valids = set()
        left = 0
        right = 0
        while right < len(nums):
            count[nums[right]] += 1
            if count[nums[right]] == degree:
                valids.add(nums[right])
            while valids and left <= right:
                answer = min(answer,right-left+1)
                if count[nums[left]] == degree:
                    valids.remove(nums[left])
                count[nums[left]] -= 1
                left += 1
                
            right += 1
        return answer
                
        
        