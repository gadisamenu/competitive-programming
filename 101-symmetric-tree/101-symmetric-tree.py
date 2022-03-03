# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stack=[root.val]
        q = deque([(root,0)])
        pre = q[-1]
        while q:
            cur= q.popleft()
            if cur[1] != pre[1]:
                if stack:
                    return False
            
            if type(cur[0]) != str:
                stack.append(cur[0].val) if not stack or  cur[0].val != stack[-1] else stack.pop()
                
                if cur[0].left or cur[0].right:
                    q.append((cur[0].left,cur[1]+1)) if cur[0].left else q.append(("n_",cur[1]+1))
                    q.append((cur[0].right,cur[1]+1)) if cur[0].right else q.append(("n_",cur[1]+1))
                else:
                    q.append(("n",cur[1]+1))
            else:
                 stack.append(cur[0]) if not stack or  cur[0] != stack[-1] else stack.pop()
            
            pre = cur
        
                    
        for v in range(len(stack)-1,-1,-1):
            if stack[v]== "n":
                stack.pop()
        return not stack

    