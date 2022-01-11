class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nexts =[nums2[0]]
        kickers ={}
        ans=[]
        for num in nums2:
            while nexts:
                if nexts[-1] < num:
                    kickers[nexts[-1]]= num
                    nexts.pop()
                    if not nexts or nexts[-1] == num:
                        nexts.append(num)
                        break
                else:
                    kickers[nexts[-1]] = -1
                    nexts.append(num)
                    break
        kickers[nums2[-1]] =-1
        for num in nums1:
            ans.append(kickers[num])
        return ans
                