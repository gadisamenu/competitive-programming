# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        queue = deque([(root, root.val)])
        goods = 0
        while queue:
            node,_max = queue.popleft()
            _max = max(_max,node.val)
            if node.val >= _max :
                goods += 1
            if node.left: queue.append((node.left,_max))
            if node.right: queue.append((node.right,_max))
            
        return goods
            