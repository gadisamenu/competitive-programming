# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        
        rem = count%k
        qnt = (count // k)
        
        ans=[]
        st = ListNode()
        st.next = head
        temp  = st
        c = qnt
        while temp.next:
            if c>0:
                temp = temp.next
                c -= 1
            else:
                c = qnt
                if rem:
                    temp = temp.next
                    rem -= 1
                ans.append(st.next)
                st.next = temp.next
                temp.next = None
                temp = st
                
        if st.next:
            ans.append(st.next)

        return ans + [None]*(k-len(ans))