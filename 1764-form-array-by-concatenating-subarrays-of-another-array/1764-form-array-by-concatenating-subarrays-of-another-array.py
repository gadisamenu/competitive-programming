class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:
        count = Counter(nums) 
        idx_grp = 0
        
        i = 0 
        j = len(groups[0])-1
        
        while j < len(nums):
            if nums[i:j+1] == groups[idx_grp]:
                idx_grp += 1
                i =j+1
                if idx_grp < len(groups):
                    j = i+ len(groups[idx_grp])-1
                else:break
            else:
                i += 1
                j += 1
                    
        return True if idx_grp == len(groups) else False
        
       