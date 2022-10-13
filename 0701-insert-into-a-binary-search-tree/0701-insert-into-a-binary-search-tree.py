# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: return TreeNode(val)
        head = root
        while True:
            if root.val < val:
                if root.right: root = root.right
                else:break
            elif root.val > val:
                if root.left: root = root.left
                else:break
                
        if root.val < val: root.right = TreeNode(val)
        else:root.left = TreeNode(val)
        return head
                
                
            
            
        