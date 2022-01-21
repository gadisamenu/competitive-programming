# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        while n and temp != None:
            temp = temp.next
            n -=1
            
        if temp != None and temp.next != None :
            temp.next = temp.next.next
    
        return head