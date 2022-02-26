# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lowB= -math.inf
        upB = math.inf
        return self.check(root,lowB,upB)
        
        
    def check(self,root,lb,ub):
        if not root:
            return True
        if lb < root.val and root.val < ub:
            if root.left and root.right:
                return self.check(root.left,lb,root.val) and self.check(root.right,root.val,ub)
            if root.left:
                return self.check(root.left,lb,root.val)
            if root.right:
                return self.check(root.right,root.val,ub)
            return True
        
        return False