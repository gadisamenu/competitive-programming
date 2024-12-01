class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:

        answer = nums[k]
        start = k
        end = k
        _min = nums[k]
        stop = False
        
        while ( start >= 0 or end < len(nums)) and not stop:
            
            if start > 0:
                if _min <= nums[start-1]:
                    start -= 1
                    
                elif end < len(nums)-1:
                    if  _min <= nums[end+1]:
                        end += 1
                        
                    elif nums[end+1] > nums[start-1]:
                        end += 1
                        _min = min(_min,nums[end])
                        
                    else:
                        start -= 1 
                        _min = min(_min,nums[start])
                        
                else:
                    start -= 1
                    _min = min(_min,nums[start])
                                         

            elif end < len(nums)-1:
                end +=1 
                _min = min(_min,nums[end])
                
            else:
                stop = True
                
            answer = max(answer,_min * (end-start+1))
                    
        return answer
            
        