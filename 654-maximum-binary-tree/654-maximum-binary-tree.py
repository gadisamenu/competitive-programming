# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
            
        def helper(start:int, end:int,stack, left = False):
            if start > end:
                return 
            if start == end:
                return TreeNode(nums[start])
            
            if left :
                stack = deque()
                for ind in range(start,end+1):
                    while stack and nums[stack[-1]] < nums[ind]:
                        stack.pop()
                    stack.append(ind)

            mx = stack.popleft() 
            return TreeNode(nums[mx],helper(start,mx-1,deque(),True),helper(mx+1,end,stack))
        
        return helper(0,len(nums)-1,deque(),True)

            
     