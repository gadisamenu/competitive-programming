# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.answer = root.val
        self.dfs(root)
        return self.answer
    
    def dfs(self,node):
        left = self.dfs(node.left) if node.left else 0
        right = self.dfs(node.right) if node.right else 0
        _max = max(left,right)
        self.answer = max(self.answer, node.val,node.val+left+right,node.val+ _max)
        return max(node.val,node.val +_max)
        
        