"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        pairing = defaultdict(lambda:None)
        root = Node(0)
        temp_o = head
        temp_n  = root
        while temp_o:
            temp_n.next = Node(temp_o.val)
            pairing[temp_o] = temp_n.next
            temp_n = temp_n.next
            temp_o = temp_o.next

        temp_n2 = root.next
        while temp_n2 and head:
            temp_n2.random = pairing[head.random]
            temp_n2=temp_n2.next
            head = head.next
        
        return root.next
            
            
        