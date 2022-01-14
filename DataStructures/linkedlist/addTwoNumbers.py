# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = ListNode()
        writing = result
        start = True
        kept = 0
        while l1 != None and l2 != None:
            sum = l1.val + l2.val + kept
            kept = sum //10
            sum = sum % 10
            if start:
                writing.val = sum
                start = False
            else:
                writing.next =ListNode(val = sum)
                writing = writing.next
            l1 = l1.next
            l2 = l2.next
        
        
        
        l1 =l1 if l1 != None else l2
                
        while kept:
            try:
                sum = kept + l1.val
                kept = sum//10
                sum = sum %10
                writing.next = ListNode(val = sum)
                writing = writing.next
                l1 = l1.next
            except AttributeError:
                writing.next = ListNode(val = kept)
                break
        
        if l1 != None:
            writing.next = l1
                                     

        return result