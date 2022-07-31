# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        
        new = ListNode()
        new.next = head
        head = new
        pre = head
        temp = head.next
        i = 1
        while temp and i < left:
            pre = temp
            temp = temp.next
            i+= 1
      
        if temp:
            tail = temp
            reverser = temp
            while temp and i <= right:
                keep = temp.next
                temp.next = reverser
                reverser = temp
                temp = keep
                
                i+= 1

            pre.next = reverser
            tail.next= temp
        
        return head.next
                 
        
            