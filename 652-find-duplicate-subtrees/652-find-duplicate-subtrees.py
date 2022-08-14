# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        memory = set()
        ans = defaultdict(int)

        def dup(node):
            if not node.left and not node.right:
                subtre = (node.val,'w')
                
            elif node.left:
                if node.right: subtre= dup(node.left)+ ('l',node.val,'r') + dup(node.right)
                else: subtre= dup(node.left) + ('l',node.val,)
            
            elif node.right:
                subtre = (node.val,'r') + dup(node.right)
            
                
            if subtre in memory:
                if not ans[subtre]:
                    ans[subtre] = node

            else: memory.add(subtre)
                
            return subtre
        
                
        dup(root)        
        return ans.values()
                
            

            
        