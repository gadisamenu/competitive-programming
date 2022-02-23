# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        merged =[]
       
        for head in lists:
            while head:
                heapq.heappush(merged,(head.val))
                head = head.next
        
        head =ListNode()
        temp =head
        
        while merged:
            temp.next =ListNode(heapq.heappop(merged))
            temp = temp.next
            
        return head.next