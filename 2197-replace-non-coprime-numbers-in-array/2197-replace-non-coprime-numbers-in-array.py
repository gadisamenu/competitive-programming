class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        ans = [nums[0]]
        ind = 1
        while ind < len(nums):          
            if ans:
                _gcd =  gcd(ans[-1],nums[ind])
                if _gcd > 1:
                    nums[ind] = lcm(nums[ind], ans.pop())
                else:
                    ans.append(nums[ind])
                    ind += 1
            else:
                ans.append(nums[ind])
                ind += 1
        return ans

