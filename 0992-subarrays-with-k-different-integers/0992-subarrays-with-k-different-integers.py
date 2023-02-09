class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def at_most_k(nums, k):
            n = len(nums)
            left, right = 0, 0

            answer = 0
            counter = defaultdict(int)

            while right < n:
                counter[nums[right]] += 1

                while len(counter) > k:
                    if counter[nums[left]] == 1:
                        counter.pop(nums[left])
                    else:
                        counter[nums[left]] -= 1
                    left += 1

                answer += right - left + 1
                right += 1

            return answer
        
        return at_most_k(nums, k) - at_most_k(nums, k-1)