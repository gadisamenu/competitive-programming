# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        q= deque([(root,0)])
        ans=[0]
        n_cl=0
        while q:
            
            cur = q.popleft()
            if len(ans)> cur[1]:
                n_cl+=1
                ans[cur[1]]+=cur[0].val
            else:
                ans[cur[1]-1]/=n_cl
                ans.append(cur[0].val)
                n_cl = 1
                
            if cur[0].left != None:q.append((cur[0].left,cur[1]+1))
            if cur[0].right != None:q.append((cur[0].right,cur[1]+1))
                
        ans[-1]/=n_cl
        return ans
        
        
   
        
        