# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        answer = 0
        stack = [(root,root.val,root.val)]
        while stack:
            node,_max,_min = stack.pop()
            answer = max(answer,abs(node.val- _min),abs(node.val - _max))
            _min = min(node.val,_min)
            _max = max(node.val,_max)
           
            if node.left: stack.append((node.left,_max,_min))
            if node.right: stack.append((node.right,_max,_min))
        
        return answer