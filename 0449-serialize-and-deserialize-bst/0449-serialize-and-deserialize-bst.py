# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        stack = [root] if root else []
        serialized = []
        while stack:
            node = stack.pop()
            if node:
                serialized.append(str(node.val)+",")
                stack.append(node.left)
                stack.append(node.right)
            else:serialized.append("*")
                
        return "".join(serialized)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        return self.helper(0,data)[1]
    
    def helper(self,i,s):
        if i == len(s) or s[i] == "*":
            return i+1,None
        start = i
        while s[i] != ",":
            i += 1
        node = TreeNode(int(s[start:i]))
        i,right = self.helper(i+1,s)
        i,left = self.helper(i,s)
        node.right = right
        node.left = left
        return i,node
            
        
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans