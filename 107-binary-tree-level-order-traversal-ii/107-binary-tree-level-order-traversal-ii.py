# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = deque()
        
        que = deque([(root,0)]) if root else []
        
        while que:
            node, lvl = que.popleft()
            if lvl >= len(ans):
                ans.appendleft([node.val])
            else:
                ans[-lvl-1].append(node.val)
         
            if node.left: que.append((node.left,lvl+1))
            if node.right: que.append((node.right,lvl+1))
                
        return ans