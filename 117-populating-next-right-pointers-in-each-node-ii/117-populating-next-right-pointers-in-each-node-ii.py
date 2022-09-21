"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root:
            head = root
            queue = deque([root])
            new = Node()
            while queue:
                level = []
                t = new
                while queue:
                    cur = queue.popleft()
                    t.next = cur
                    if cur.left: level.append(cur.left)
                    if cur.right: level.append(cur.right)
                    t = t.next
                queue.extend(level)
            new.next = None
        return root

                
                
        
                
            
                