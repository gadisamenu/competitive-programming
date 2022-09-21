# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        ans = []
        
        def dfs(root,tgt):
            tgt -= root.val
            if root.left or root.right:
                ret= []
                if root.left: ret.extend(dfs(root.left,tgt))
                if root.right: ret.extend(dfs(root.right,tgt))
    
                for i in ret:
                    ans[i].appendleft(root.val)
                return ret
            if tgt: return []
            ans.append(deque([root.val]))
            return [len(ans)-1]
        
        if root: dfs(root,targetSum)
        return ans
            