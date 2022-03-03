# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        que = deque([(root,1)])
        
        while que:
            cur = que.popleft()
            
            if cur[0].left: que.append((cur[0].left,cur[1]+1))
            if cur[0].right: que.append((cur[0].right,cur[1]+1))
                
        return cur[1]
        
        