class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lgth= len(nums)
        right_product = [1]
        for ind in range(lgth):
            right_product.append(right_product[-1]*nums[lgth-ind-1])
        
          
    
        
        answer =[]
        left_product = 1
        for ind  in range(lgth):
            if ind:
                left_product *= (nums[ind-1]) 
                
            if ind == lgth -1:
                answer.append(left_product)
            else:
                answer.append(left_product*right_product[lgth-ind-1])
        return answer