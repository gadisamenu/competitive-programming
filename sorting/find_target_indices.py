class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        ind =[]
        exist = False
        try:
            ind.append(nums.index(target))
            exist=True
        except ValueError:
            pass
        if exist:
            while ind[-1]+1 < len(nums) and  target == nums[ind[-1]+1]:
                ind.append(ind[-1]+1)
        return ind
    
        
            