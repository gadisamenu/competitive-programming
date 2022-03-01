# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.tilt_sum = 0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 0
        
        def dfs(node):
            left_sum = dfs(node.left) if node.left else 0
            right_sum = dfs(node.right) if node.right else 0
            
            self.tilt_sum += abs(left_sum-right_sum)
            
            return (node.val+left_sum + right_sum)
        
        dfs(root)
        
        return self.tilt_sum
 