# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
           
        def backtracking(lv,hv):
            if lv > hv: return [None]
            if lv == hv: return [TreeNode(val=lv)]
            ans = []
            for v in range(lv,hv+1):
                left = backtracking(lv,v-1)
                right = backtracking(v +1,hv)
                for l in left:
                    for r in right:
                        n = TreeNode(val = v)
                        n.left = l
                        n.right = r
                        ans.append(n)
                
            return ans
        
        return backtracking(1,n)
            