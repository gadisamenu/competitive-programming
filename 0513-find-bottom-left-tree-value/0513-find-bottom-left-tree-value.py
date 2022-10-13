# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        stack = [(0,root)]
        ans = [0,root.val]
        while stack:
            lv,node = stack.pop()
            if lv > ans[0]:
                ans[0] = lv 
                ans[1] = node.val
            if node.right:stack.append((lv+1,node.right))
            if node.left:stack.append((lv+1,node.left))
            
        return ans[1]
            
            