# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list1 = []
        temp = headA
        while temp:
            list1.append(temp)
            temp = temp.next
        
        
        list2 = []
        temp = headB
        while temp:
            list2.append(temp)
            temp = temp.next
        
        min_lgth = min(len(list1),len(list2))
        index = -1
        answer = None
        while abs(index) <= min_lgth:
            if list1[index] != list2[index]:
                break
            answer= list1[index]
            index -= 1
            
        return answer
    
    
                
            
            
            