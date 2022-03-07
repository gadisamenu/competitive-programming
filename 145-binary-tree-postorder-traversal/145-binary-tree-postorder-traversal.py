# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.ans =[]
        def dfs(node):
            if node.left:dfs(node.left)
            if node.right:dfs(node.right)
            self.ans.append(node.val)
    
        dfs(root)
        return self.ans