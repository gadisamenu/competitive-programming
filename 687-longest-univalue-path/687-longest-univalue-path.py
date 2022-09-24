# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            left = dfs(node.left) if node.left else [1001,0]
            right = dfs(node.right) if node.right else [1001,0]
            if node.val == right[0]:
                if node.val == left[0]: 
                    self.ans = max(left[1] + right[1],self.ans)
                    left[1] =  1 + max(right[1],left[1])
                    return left
                right[1]+=1
                return  right
            
            if node.val == left[0]: 
                left[1]+=1
                return left
            
            self.ans = max(left[1]-1,right[1]-1,self.ans)
            return [node.val,1]
                
        if root:
            self.ans = max(dfs(root)[1]-1,self.ans)
        return self.ans
            
        
                                                    
                            
                
                