class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        nums.append("a")
        j = 0
        i = 0
        answer = 0
        while j < len(nums):
            if nums[j] == 0:
                j += 1
            else:
                answer += ((j-i)*(j-i+1))// 2
                while j < len(nums) and nums[j] != 0:
                    j+= 1
                i = j
        return answer