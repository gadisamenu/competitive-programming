# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from sortedcontainers import SortedList
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue  = deque([(root,0,0)])
        ans = defaultdict(lambda: defaultdict(SortedList))
        
        while queue:
            node,r,c = queue.popleft()
            ans[c][r].add(node.val)
            r+= 1
            if node.left: queue.append((node.left,r,c-1))
            if node.right: queue.append((node.right,r,c+1))
  
        cols = sorted(ans)
        result = []
        for col in cols:
            c = []
            for r in ans[col]:
                c.extend(ans[col][r])
            result.append(c)
        return result
            
            
        