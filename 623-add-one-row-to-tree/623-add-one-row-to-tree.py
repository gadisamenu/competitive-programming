# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val,root)

        depth -= 1
        
        def dfs(root,height):
            if height  == depth:
                new = TreeNode(val,root.left)
                root.left = new
                new = TreeNode(val,None,root.right)
                root.right = new
                return 
            if root.left:dfs(root.left,height+1)
            if root.right:dfs(root.right,height+1)
        
        dfs(root,1)
        return root
                
