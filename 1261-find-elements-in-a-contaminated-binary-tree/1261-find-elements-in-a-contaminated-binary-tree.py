# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.elements = set()
        root.val =0
        stack = [root]
        while stack:
            node =stack.pop()
            self.elements.add(str(node.val))
    
            if node.left:
                node.left.val = 2*node.val +1
                stack.append(node.left)
            if node.right:
                node.right.val = 2*node.val  +2
                stack.append(node.right)

    def find(self, target: int) -> bool:
        return True if str(target) in self.elements else False

        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)