# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        index = {}
        for i,r in enumerate(inorder):
            index[r] = i
            
        def dfs(i,si,sj):
            if si > sj: return None
            if si==sj: return  TreeNode(preorder[i])
            ind = index[preorder[i]]
            
            return TreeNode(preorder[i], dfs(i+1,si,ind-1), dfs(i+(ind-si)+1,ind+1,sj))
        
        return dfs(0,0,len(preorder)-1)