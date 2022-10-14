# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pre= head
        fast = head
        slow = head
        
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next
        
        pre.next = None
        
        if slow != fast:
    
            temp = slow.next
            slow.next = None
            while temp:
                keep = slow
                slow = temp
                temp = temp.next
                slow.next = keep


            temp = head
            pre = temp
            while slow and temp:
                pre = slow
                keep = temp.next
                temp.next = slow
                slow = slow.next
                temp.next.next = keep
                temp = temp.next.next

            if slow:pre.next = slow
            
        
                
        
            
            