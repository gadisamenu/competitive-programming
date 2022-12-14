class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        lgth = len(nums)
        diff = float("inf")
        answer = 0
        
        for fst in range(lgth):
            snd = 0
            trd = lgth-1
            while snd < trd:
                if fst == snd:
                    snd += 1
                elif fst == trd:
                    trd -= 1
                else:
                    _sum = nums[fst] + nums[snd]+ nums[trd]
            
                    distance = _sum - target
                    if abs(distance) < diff:
                        answer = _sum
                        diff = abs(distance)
                
                    if distance > 0:
                        trd -= 1
                    else:
                        snd += 1
        return answer