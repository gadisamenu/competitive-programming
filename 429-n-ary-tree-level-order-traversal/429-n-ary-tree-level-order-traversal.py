"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        queue = deque([(root,0)]) if root else None
        pre = -1
        ans = []
        while queue:
            node,lv = queue.popleft()
            if lv == pre:
                ans[-1].append(node.val)
            else:
                ans.append([node.val])
                pre = lv
            lv += 1
            for ch in node.children:
                queue.append((ch,lv))
        return ans
            