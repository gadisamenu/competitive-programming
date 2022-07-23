# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        nodes = []
        while head:
            nodes.append(head.val)
            head = head.next
            
        nodes.sort()
        head = ListNode()
        temp = head
        
        for node in nodes:
            temp.next = ListNode(node)  
            
            temp =  temp.next
            
        return head.next
            