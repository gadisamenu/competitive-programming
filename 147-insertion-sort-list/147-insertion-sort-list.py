# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp =head
        temp2 = head
        nodes = []
        while temp:
            nodes.append(temp.val)
            temp = temp.next
        print(nodes)
        
        nodes.sort()
        
        temp2.val= nodes[0]
        for i in range(1,len(nodes)):
            temp2.next = ListNode(nodes[i])
            temp2 = temp2.next
            
        return head
        
            
#         newhead = ListNode(None)
#         newhead.next = head
#         head =newhead
            
#         temp = head
       
#         while temp and  temp.next:
            
#             temp2 = head 
#             change =False

#             while id(temp2.next) != id(temp.next):    
#                 if temp2.next.val >= temp.next.val:
#                     keep = temp2.next
#                     keep2 = temp.next.next
#                     temp2.next = temp.next
#                     temp.next.next = keep
#                     temp.next = keep2
#                     change = True
#                     break
        
        

#                 temp2 = temp2.next
            
#             if not change:
#                 temp = temp.next
#                 change = False
            
#         head = head.next
        return head

