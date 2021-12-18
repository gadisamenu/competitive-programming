class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key=lambda string:int(string))
        if k <= len(nums):
            return nums[-k]
      