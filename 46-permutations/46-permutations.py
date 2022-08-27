class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = set()
        def rec():
            if len(visited) < len(nums):
                ans = []
                for n in nums:
                    if n not in visited:
                        visited.add(n)
                        ret = rec()
                        for m in ret:
                            m.appendleft(n)
                            ans.append(m)
                        visited.remove(n)
                return ans
            else:
                return [deque()]
        return rec()
            