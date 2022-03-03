# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        tree_q = deque([q])
        tree_p = deque([p])
        while tree_q and tree_p:
            p = tree_p.popleft()
            q = tree_q.popleft()
            if p and q:
                if p.val != q.val:
                    return False
                tree_p.append(p.left) if p.left else tree_p.append(0)
                tree_p.append(p.right) if p.right else tree_p.append(0)
                tree_q.append(q.left) if q.left else tree_q.append(0)
                tree_q.append(q.right) if q.right else tree_q.append(0)
            else:
                if p != q:
                    return False
            
            
        return True
            