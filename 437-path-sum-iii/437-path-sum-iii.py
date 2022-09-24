# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count = 0
        self.sum = 0
        self.prefix = defaultdict(int)
        self.prefix[0]+=1
        
        def dfs(node):
            self.sum += node.val
            self.count += self.prefix[self.sum -targetSum]
            self.prefix[self.sum] += 1
            if node.left: dfs(node.left)
            if node.right: dfs(node.right)
            self.prefix[self.sum] -=1
            self.sum -= node.val
  
        if root: dfs(root)
        return self.count
               