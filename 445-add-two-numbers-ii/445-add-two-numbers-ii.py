# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        que1  = deque()
        que2  = deque()
        
        while l1:
            que1.appendleft(l1.val)
            l1 = l1.next
        while l2:
            que2.appendleft(l2.val)
            l2 = l2.next
        
        head  = None
        lgth = min(len(que1),len(que2))
        keep = 0
        for i in range(lgth):
            head =  ListNode((que1[i]+que2[i]+keep)%10,head)
            keep = (que1[i]+que2[i]+keep)//10
      
        if len(que1) == lgth:
            for i in range(lgth,len(que2)):
                head =  ListNode((que2[i]+keep)%10,head)
                keep = (que2[i]+keep)//10
            
        else:
            for i in range(lgth,len(que1)):
                head =  ListNode((que1[i]+keep)%10,head)
                keep = (que1[i]+keep)//10

        if keep > 0:
            head = ListNode(keep,head)
            
        return head
        