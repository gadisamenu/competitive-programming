# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        end = head
        for i in range(n+1):
            if not end: return head.next
            end = end.next
            
        temp = head
        while end:
            end = end.next
            temp = temp.next
            
        temp.next = temp.next.next
        return head