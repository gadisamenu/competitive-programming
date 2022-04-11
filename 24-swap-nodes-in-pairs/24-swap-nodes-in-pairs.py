# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        head,head.next = ListNode(),head
        temp = head
        first = head.next
        second = first.next
        while first and second:
            first.next = second.next
            second.next = first
            temp.next = second
            temp= second.next
            first = first.next
            if first:
                second = first.next
        return head.next
            
        