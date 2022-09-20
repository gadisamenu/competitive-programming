# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = None
        temp = head
        while temp:
            if temp.val == None:
                ans = temp
                break
            temp.val = None
            temp = temp.next
            
        return ans