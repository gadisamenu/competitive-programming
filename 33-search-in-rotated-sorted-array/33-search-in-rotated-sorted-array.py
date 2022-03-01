class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def k_finder():
            left = 0
            right = len(nums)-1
            
            while left < right-1:
                mdl = left + (right-left)//2
                val = nums[mdl]
                
                if nums[0]  < val and nums[-1] < val:
                    left = mdl
                elif nums[0] > val and nums[-1] > val:
                    right = mdl
                else:
                    return right
            return left
        
        
        def  binarySearch(num,target):       
            left = 0
            right = len(num)-1

            while left <= right:
                mdl = left + (right-left)//2

                peaked = num[mdl]

                if peaked < target:
                    left = mdl+1

                elif peaked > target:
                    right= mdl -1
                else:
                    return mdl
            return None

        k =k_finder()
        
        frst = binarySearch(nums[:k+1],target) 
        scnd =binarySearch(nums[k+1:],target) 
            
        if frst != None:
            return frst
        if scnd != None:
            return scnd +k + 1
        return -1
        
        
        
                