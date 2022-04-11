# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        stack = []
        while fast and fast.next:
            stack.append(slow.val)
            fast = fast.next.next
            slow = slow.next
        keep = None
        while stack and  slow:
            if slow.val == stack[-1]:
                stack.pop()
                slow = slow.next
            elif keep == None:
                keep = slow.val
                slow = slow.next
            else:
                return False
            
        return False if stack else True
                
                
            
                
        
        