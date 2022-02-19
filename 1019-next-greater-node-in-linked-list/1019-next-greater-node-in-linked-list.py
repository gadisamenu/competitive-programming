# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        kickers = {}
        dcr = []
        ans = []
        temp = head
        lgth = 0
        while temp:
            while dcr and  dcr[-1][0] < temp.val:
                kickers[dcr.pop()[1]] = temp.val
            dcr.append([temp.val,lgth])
            lgth +=1
            temp = temp.next
            
            
        for i in range(lgth):
            try:
                ans.append(kickers[i])
            except:
                ans.append(0)
        return ans