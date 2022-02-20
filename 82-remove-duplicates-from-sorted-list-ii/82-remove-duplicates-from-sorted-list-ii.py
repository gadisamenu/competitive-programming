# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        head = ListNode()
        head.next = temp
        
        temp = head.next
        keep = head
        
        while temp and  temp.next:
            if temp.val == temp.next.val:
                while temp.next and temp.val == temp.next.val:
                    temp.next = temp.next.next
                keep.next = temp.next
                temp = keep.next
                
            else:
                keep = temp
                temp = temp.next
                
        return head.next