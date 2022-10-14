# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head
        pre = slow
        
        while fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        
        if fast and fast.next: slow.next = slow.next.next
        elif pre.next: pre.next = pre.next.next
        else:head = None
            
        return head
    
    
        