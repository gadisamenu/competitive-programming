class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        length = len(nums)
        k = length//3
        ans =[]
        nums.sort()
        ind =0
        while ind < length:
            if ind >= length -1 and k != 0:
                break
            if ind+k <= length-1:
                if nums[ind]== nums[ind+k]:
                    ans.append(nums[ind])
                    ind += (k+1)
            else:
                ind +=1
        if len(ans) ==2:
            if ans[0] == ans[1]:
                ans.remove(ans[1])
        return ans