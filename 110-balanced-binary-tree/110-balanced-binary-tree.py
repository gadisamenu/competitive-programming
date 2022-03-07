# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.valid=True
        def dfs(node):
            left = dfs(node.left) if node.left else 0
            right = dfs(node.right) if node.right else 0
            if abs(left - right) > 1:
                self.valid=False
            return  max(left,right)+1
        dfs(root)
        return self.valid
        