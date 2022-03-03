# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        que = deque([(root,0)])
        ans = [[]]
        while que:
            cur = que.popleft()
            if len(ans)>cur[1]:
                ans[cur[1]].append(cur[0].val)
            else:
                ans.append([cur[0].val])
            if cur[0].left: que.append((cur[0].left,cur[1]+1))
            if cur[0].right: que.append((cur[0].right,cur[1]+1))
        return ans