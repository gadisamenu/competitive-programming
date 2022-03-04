# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        self.deep= 0
        self.c_anc=root
        
        def dfs(node,lv):
            if not node.left and not node.right:
                return lv
                
            left = dfs(node.left,lv+1) if node.left else None
            right = dfs(node.right,lv+1) if node.right else None
            
            if left != None and right != None:
                if left == right  and left >= self.deep :
                    self.deep =left
                    self.c_anc = node
                    return left
                return left if left > right else right
              
            elif left:
                if left > self.deep:
                    self.deep  = left
                    self.c_anc = node.left
                return left
            elif right:
                if right > self.deep:
                    self.deep  = right
                    self.c_anc = node.right
                return right

            print(left,right,lv)
                
        dfs(root,0)
        
        return self.c_anc
            
                
        