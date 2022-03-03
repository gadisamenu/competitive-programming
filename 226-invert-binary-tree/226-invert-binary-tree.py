# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        que = deque([(root)])
        while que:
            cur= que.popleft()
            cur
            if cur.left or cur.right:
                cur.left,cur.right = cur.right,cur.left
                if cur.left: que.append(cur.left)
                if cur.right: que.append(cur.right)
                
        return root