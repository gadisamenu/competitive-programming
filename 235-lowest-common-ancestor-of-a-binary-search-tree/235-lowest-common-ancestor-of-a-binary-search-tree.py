# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        def dfs(node):
            ans = 0
            if node.val == p.val or node.val == q.val: ans += 1
                
            if node.left and (node.val > q.val or node.val > p.val): ans += dfs(node.left)
            
            if node.right and (node.val < q.val or node.val < p.val): ans += dfs(node.right)
                
            if ans == 2:
                self.ans = node
                return 0
            return ans
        
        dfs(root)
        return self.ans
            