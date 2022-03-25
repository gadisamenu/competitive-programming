# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        que = deque([(root,0)])
        pre_level=-1 
        ans =[]
        while que:
            node,level = que.popleft()
            
            if pre_level == level:
                if ans[level] < node.val:
                    ans[level] = node.val
            else:
                ans.append(node.val)
                pre_level = level
                
            if node.left: que.append((node.left,level+1))
            if node.right: que.append((node.right,level+1))
                
        return ans
                

        
        