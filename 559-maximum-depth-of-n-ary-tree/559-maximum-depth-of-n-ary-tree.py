"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        def dfs(node):
            if not node.children:
                return 1
            else:
                cur_depth=0
                for child in node.children:
                    cur_depth = max(dfs(child),cur_depth)
                return cur_depth+1
            
        return dfs(root)
