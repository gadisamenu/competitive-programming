# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        @cache
        def dp(node,_list):
            if not _list:
                return True
            if not node:
                return False
            if node.val == _list.val:
                if dp(node.left,_list.next) or dp(node.right,_list.next):
                    return True
            return dp(node.left,head) or dp(node.right,head) 
        
        return dp(root,head)