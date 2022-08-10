# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def helper(node):
            ans = False if node.val == 1 else True
            if node.left:
                left = helper(node.left)
                if left: node.left  = None
                ans &= left
                
            if node.right:
                right = helper(node.right)
                if right: node.right = None
                ans&=right
            return ans
        
        root = TreeNode(0,root)
        
        helper(root)
        return root.left
            
        