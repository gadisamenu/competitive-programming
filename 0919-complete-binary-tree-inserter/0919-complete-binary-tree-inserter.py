# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.queue = deque([root])
        while self.queue[0].left and self.queue[0].right:
                node = self.queue.popleft()
                if node.left: self.queue.append(node.left)
                if node.right: self.queue.append(node.right)
        if self.queue[0].left:self.queue.append(self.queue[0].left)
            
    def insert(self, val: int) -> int:
        new = TreeNode(val)
        answer= self.queue[0]
        
        if not answer.left:
            answer.left = new
        else:
            answer.right = new
            self.queue.popleft()
            
        self.queue.append(new)
        return answer.val
        
        
        

    def get_root(self) -> Optional[TreeNode]:
        return self.root 
   

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()