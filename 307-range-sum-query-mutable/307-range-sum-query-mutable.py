class Node:
    def __init__(self,left,right,val = 0):
        self.left = left
        self.right = right
        self.val = val
        self.left_node = None
        self.right_node = None

class NumArray:

    def __init__(self, nums: List[int]):
        def segmentTree(i,j):
            if i== j:
                return Node(i,j,nums[i])
            
            left = segmentTree(i,(i+(j-i)//2))             
            right = segmentTree((i+(j-i)//2)+1,j)
            node = Node(i,j,left.val+right.val)
            node.left_node = left
            node.right_node = right
            
            return node
            
        self.treeRoot = segmentTree(0,len(nums)-1)
        
    def update(self, index: int, val: int) -> None:
        def update(node):
            if node.left == node.right:
                diff = val - node.val
                node.val = val
                return diff
            
            if node.left_node.left  <= index <= node.left_node.right :
                diff = update(node.left_node)
            else:
                diff = update(node.right_node)
            node.val += diff
            return diff
        
        update(self.treeRoot)
            
            
    def sumRange(self, left: int, right: int) -> int:
        
        def find_sum(node):
            
            if left <= node.left  and right >= node.right:
                return node.val
            
            ans = 0
            if left <= node.left_node.right:
                ans += find_sum(node.left_node)
            
            if right >= node.right_node.left:
                ans += find_sum(node.right_node)
            
            return ans
            
        return find_sum(self.treeRoot)
            
            

                

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)