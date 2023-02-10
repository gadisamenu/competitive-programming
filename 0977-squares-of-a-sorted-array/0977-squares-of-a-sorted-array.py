class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        i= 0 
        j = len(nums)-1
        ans = deque()
        while i<=j:
            left = nums[i]**2
            right = nums[j]**2
            if left < right:
                ans.appendleft(right)
                j-=1
            else:
                ans.appendleft(left)
                i+=1
        return ans