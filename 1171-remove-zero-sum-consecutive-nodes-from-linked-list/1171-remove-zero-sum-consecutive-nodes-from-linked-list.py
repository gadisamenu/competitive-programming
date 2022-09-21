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
            temp = temp.next
            if _sum in prefix:
                zeros.append((prefix[_sum]+1,count))
            prefix[_sum] = count
                    
        
        valid = []
        end = -1
        zeros.sort(key=lambda x: x[0])
        for z in zeros:
            if end < z[0]:
                valid.append(z)
                end = z[1]
                
        rem = set()
        for v in valid:
            rem.update([x for x in range(v[0],v[1]+1)])
    
        new_h =ListNode()
        new_h.next = head
        temp = new_h
        count = 0
        while temp.next:
            if count in rem:
                temp.next = temp.next.next
            else:
                temp = temp.next
            count += 1
        
        return new_h.next
                
                
        
        
        
            