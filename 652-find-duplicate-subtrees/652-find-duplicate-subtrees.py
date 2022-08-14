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
            
            left = dup(node.left) if node.left else ""
            right = dup(node.right) if node.right else ""
            
            subtre =  str(node.val) + "l"+ left + "r"+ right            
                
            if subtre in memory:
                if not ans[subtre]:
                    ans[subtre] = node

            else: memory.add(subtre)
                
            return subtre
        
                
        dup(root)        
        return ans.values()
                
            

            
        