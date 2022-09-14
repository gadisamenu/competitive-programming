# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        path = defaultdict(int)
        self.ans = 0
        evens = set()
        
        def dfs(node):
            path[node.val] += 1
            if node.val in evens:
                evens.remove(node.val)
            elif path[node.val] %2 == 0:
                    evens.add(node.val)
            if not(node.left) and not(node.right):
                if len(path) - len(evens) <= 1:
                        self.ans += 1
            else:  
                if node.left: dfs(node.left)
                if node.right: dfs(node.right)
            
            if path[node.val] == 1:
                path.pop(node.val)
            else: path[node.val] -= 1
                
            if node.val in evens:
                evens.remove(node.val)
            elif node.val in path and  path[node.val] %2 == 0:
                evens.add(node.val)
                
        dfs(root)
        return self.ans
            
            
            
                
            