# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        
        def dfs(node,val =0):
            if node.right: val = dfs(node.right,val)
            node.val += val
            val = node.val
            if node.left: val =  dfs(node.left,node.val)
            return val
                
        dfs(root)
        return root
                
        
                