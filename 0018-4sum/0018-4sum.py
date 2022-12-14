class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        lgth = len(nums)
        nums.sort()
        answer = set()
        
        for frst in range(lgth-3):
            for snd in range(frst+1,lgth-2):
                trd = snd + 1
                frth = lgth -1
                while trd < frth:
                    _sum = nums[frst] + nums[snd] + nums[trd] + nums[frth]
                    if target == _sum:
                        quadruplets = (nums[frst],nums[snd],nums[trd],nums[frth])
                        if quadruplets not in answer:
                            answer.add(quadruplets)
                        trd += 1
                    
                    elif target > _sum:
                        trd += 1
                    else:
                        frth  -= 1
            
        return answer