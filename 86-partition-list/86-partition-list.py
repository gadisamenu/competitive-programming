# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        new = ListNode()
        new.next= head
        head = new
        temp = head.next
        end_first = head
        scnd_part = None
        
        while temp:
            if temp.val >= x:
                scnd_part = temp
                break
            end_first = temp
            temp = temp.next
            
        if scnd_part:
            keep = scnd_part
            pre = scnd_part
            scnd_part = scnd_part.next
            while scnd_part:
                if scnd_part.val < x:
                    cut = scnd_part
                    pre.next = scnd_part.next
                    cut.next = None
                    end_first.next = cut
                    end_first = end_first.next

                else:
                    pre = scnd_part
                scnd_part = pre.next

            end_first.next = keep
        
        return head.next
            
            
            
        
        