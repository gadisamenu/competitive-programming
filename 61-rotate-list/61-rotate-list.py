# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:return None
        count =0
        temp = head
        while temp:
            count +=1
            temp = temp.next
        
        k %=count
        if k == 0:return head
        
        temp = head
        while temp:
            if count == k+1: break
            temp = temp.next
            count -= 1
            
        new_head = temp.next
        temp.next = None
        
        temp = new_head
        while temp.next:
            temp = temp.next
        temp.next = head
        
        return new_head
        
        
                
