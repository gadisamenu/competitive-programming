# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root.val < val:
            return TreeNode(val,root)
        
    
        
        def dfs(node):
            if not node.right:
                node.right = TreeNode(val)
            elif node.right.val < val:
                node.right = TreeNode(val,node.right)
            else:
                dfs(node.right)
               
        dfs(root)
        return root
                