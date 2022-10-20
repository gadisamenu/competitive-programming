# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        
        @cache
        def dfs(node,taken= False):
            if not node:
                return 0
            
            if not taken:
                node_taken = node.val + dfs(node.left,True) + dfs(node.right,True)
                node_not_taken = dfs(node.left) + dfs(node.right)
                return max(node_taken,node_not_taken)
#                
            return dfs(node.left) + dfs(node.right)
        
        return dfs(root)