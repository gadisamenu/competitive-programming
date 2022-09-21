# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = {0:-1}
        zeros = []
        _sum =0
        temp = head
        count=  -1
        while temp:
            count += 1
            _sum += temp.val
            if _sum in prefix:  zeros.append((prefix[_sum]+1,count))
            prefix[_sum] = count
            temp = temp.next
                    
        rem = set()
        end = -1
        zeros.sort(key=lambda x: x[0])
        for z in zeros:
            if end < z[0]:
                rem.update([x for x in range(z[0],z[1]+1)])
                end = z[1]
    
        new_h =ListNode(0,head)
        temp = new_h
        count = 0
        while temp.next:
            if count in rem: temp.next = temp.next.next
            else:  temp = temp.next
            count += 1
        
        return new_h.next
                
                
        
        
        
            