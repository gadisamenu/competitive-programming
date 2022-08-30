# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = OrderedDict()
        
        que = deque([(root,0)]) if root else None
        
        while que:
            node,lvl = que.popleft()
            if lvl not in ans:
                ans[lvl] = node.val
            if node.right: que.append((node.right,lvl+1))
            if node.left: que.append((node.left,lvl+ 1))
    
        return ans.values()