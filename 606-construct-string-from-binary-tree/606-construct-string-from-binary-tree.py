# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        
        def dfs(node):
            ans=[str(node.val)]
            left = dfs(node.left)if node.left else ""
            if left: 
                ans.append("(")
                ans.extend(left)
                ans.append(")")
            right = dfs(node.right) if node.right else ""
            if right:
                if not left:
                    ans.append("()")
                ans.append("(")
                ans.extend(right)
                ans.append(")")
            return  ans
        
        return "".join(dfs(root))
  