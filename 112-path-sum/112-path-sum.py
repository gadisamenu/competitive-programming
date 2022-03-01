# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.path_sum = 0
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
       
        def dfs(node):
            
            if not node.left and not node.right:
                return (self.path_sum + node.val) == targetSum
                
            self.path_sum+=node.val
            
            left = dfs(node.left) if node.left else False
            right =  dfs(node.right) if node.right else False
            
            self.path_sum -= node.val
            ans = left or right
            return ans
            
            
        return dfs(root)

        