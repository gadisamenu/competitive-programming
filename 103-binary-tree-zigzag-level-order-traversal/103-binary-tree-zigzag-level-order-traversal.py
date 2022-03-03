# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q =  deque([(root,0)])
        ans=[[]]
        while q:
            cur = q.popleft()
            if len(ans)> cur[1]:
                ans[cur[1]].append((cur[0].val))
            else:
                if (cur[1]-1)%2== 0:
                    ans[cur[1]-1].reverse()
                ans.append([cur[0].val])
            
            
            if cur[0].right: q.append((cur[0].right,cur[1]+1))
            if cur[0].left: q.append((cur[0].left,cur[1]+1))
                
        if (cur[1])%2== 0:
                    ans[cur[1]].reverse()
        return ans
            
        
        