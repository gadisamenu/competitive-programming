class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        
        for idx in range(len(nums)):
            nums[idx] = (nums[idx],idx)
    
        
        
        def merge_sort(nums:list)->list:
            
            if len(nums) > 1:
                mdl = len(nums)//2
                left = merge_sort(nums[:mdl])
                right = merge_sort(nums[mdl:])
                
                _out = []
                
                i,j = 0, 0
                used = 0
                while i < len(left) and j < len(right):
                    if left[i][0] <= right[j][0]:
                        _out.append(left[i])
                        ans[left[i][1]] += (j-used)
                        used = 0
                        i += 1
                        
                    else:
                        used += 1
                        ans[left[i][1]] += 1
                        _out.append(right[j])
                        j += 1
                

                while i < len(left):
                    _out.append(left[i])
                    ans[left[i][1]] += (j-used)
                    used = 0
                    i+= 1

                while j < len(right):
                    _out.append(right[j])
                    j+= 1
                    
                # print(_out,ans)
                
        
                return _out
            
            else:
                return nums
                    
            
        merge_sort(nums)
    
        return ans