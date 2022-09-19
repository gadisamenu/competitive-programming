# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        
        def dfs(lw,node,hgh):
            if not node: return 
            if node.val < lw:
                return dfs(lw,node.right,hgh)
    
            if hgh < node.val:
                return dfs(lw,node.left,hgh)
              
            node.right = dfs(node.val,node.right,hgh)
            node.left = dfs(lw,node.left,node.val)
            return node
             
        
        return dfs(low,root,high)

                
                    
                
            