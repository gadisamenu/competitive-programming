# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i,r in enumerate(inorder):
            index[r] = i
            
        def dfs(j,si,sj):
            if si > sj: return None
            if si==sj:return  TreeNode(postorder[j])
            ind = index[postorder[j]]
            return TreeNode( postorder[j], dfs(j-(sj-ind+1),si,ind-1), dfs(j-1,ind+1,sj))
        
        return dfs(len(postorder)-1,0,len(postorder)-1)
    
 