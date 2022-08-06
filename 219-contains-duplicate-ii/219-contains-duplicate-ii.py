class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = set(nums[:k+1])
        i = 0 
        j = min(i +k,len(nums) -1)        
        while j < len(nums):
            if  len(visited) < j - i+1:
                return True
            visited.remove(nums[i])
            if j+ 1 < len(nums):
                visited.add(nums[j+1])
            i+= 1
            j+= 1
            
        return False