# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1: return TreeNode(val,root)
        
        depth -= 1
        
        queue = deque([(root,1)])
        
        while queue:
            node, height = queue.popleft()
            if height == depth:
                new = TreeNode(val,node.left)
                node.left = new
                new = TreeNode(val,None,node.right)
                node.right = new
                continue
            
            if node.left: queue.append((node.left, height+1))
            if node.right: queue.append((node.right, height+1))
                
        return root
                

                
