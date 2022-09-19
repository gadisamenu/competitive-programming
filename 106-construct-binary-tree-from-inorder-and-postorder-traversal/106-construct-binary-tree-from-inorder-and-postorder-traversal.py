# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        def dfs(inord,post):
            if not post: return None
            ind = inord.index(post[-1])            
            return TreeNode(post[-1], dfs(inord[:ind],post[:ind]), dfs(inord[ind+1:],post[ind:-1]))
        
        return dfs(inorder,postorder)
    
 