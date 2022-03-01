# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.sum_nodes= 0
        def dfs(node,prnt,gprnt):
            if gprnt:
                self.sum_nodes+= node.val
                
            gprnt=prnt
            prnt= 1 if node.val%2 ==0 else 0   
            
            if node.left:
                dfs(node.left,prnt,gprnt)
            if node.right:
                dfs(node.right,prnt,gprnt)
                
        dfs(root,0,0)
        
        return self.sum_nodes