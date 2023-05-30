# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        numbers = []
        def collect(node):
            numbers.append(node.val)
            if node.left: collect(node.left)
            if node.right: collect(node.right)
                
        collect(root)
        numbers.sort(reverse = True)
        def assign(node):
            if node.left: assign(node.left)
            node.val = numbers.pop()
            if node.right:assign(node.right)
                
        assign(root)