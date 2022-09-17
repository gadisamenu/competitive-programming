class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        count = Counter(nums)
        ans = set()
        if count[0] >= 3: 
            ans.add((0,0,0))
        nums=list(set(nums))
        nums.sort()
        lgth = len(nums)
        
        for i in range(lgth):
            for j in range(i+1,lgth):
                target = 0 - nums[i] - nums[j]
                ind =  bisect_left(nums,target)
                if 0 <= ind < lgth and nums[ind] ==target:
                    if i == ind and count[nums[i]]> 1:
                        ans.add((nums[ind],nums[i],nums[j]))
                    elif  j == ind and count[nums[j]] > 1:
                        ans.add((nums[i],nums[j],nums[ind]))
                    elif i != ind and j != ind:
                        if ind < i:
                            ans.add((nums[ind],nums[i],nums[j]))
                        elif ind > j:
                            ans.add((nums[i],nums[j],nums[ind]))
                        else:
                            ans.add((nums[i],nums[ind],nums[j]))
        return ans