class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        _max = len(nums)-1
        n = len(nums)-2
        while n  > -1:
            if nums[n] < nums[_max]:
                _max = n
                break
            _max = n
            n -= 1
            
        if n > -1:
            for n in range(len(nums)-1,-1,-1):
                if nums[n] > nums[_max]:
                    nums[n],nums[_max]= nums[_max],nums[n]
                    break
        else: _max = n

        i = _max+1
        j = len(nums)-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
            
        
            
                
                
        
            