# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        even = ListNode()
        ev_temp = even
        temp = head
        while True:
            ev_temp.next = temp.next
            ev_temp = ev_temp.next
            if temp.next and temp.next.next:
                temp.next = temp.next.next
                temp = temp.next
            else:
                break
            
        temp.next = even.next
        return head