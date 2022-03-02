# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def reverser(node):
            new = None
            while node:
                temp2 = node
                node = node.next
                temp2.next=new
                new = temp2
            return new
        
        new = head
        head= ListNode()
        head.next= new
     
        
        start= head
        temp = head
        n_nodes= 0
        while temp:
            n_nodes+=1
            if n_nodes > k:
                srt= start.next
                save_nxt= temp.next
                temp.next = None
                start.next = reverser(srt)
                srt.next = save_nxt
                temp = start =srt
                n_nodes = 0
            else:
                temp = temp.next
        return head.next
            
