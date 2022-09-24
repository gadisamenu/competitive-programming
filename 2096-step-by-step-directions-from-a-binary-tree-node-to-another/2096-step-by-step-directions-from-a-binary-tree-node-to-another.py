# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        self.ans = []
        def dfs(node,dr):
            if node:            
                left = dfs(node.left,"L")
                right = dfs(node.right,"R")
                
                if node.val == startValue:
                    if left:
                        self.ans = [left[::-1]]
                        return
                    if right:
                        self.ans = [right[::-1]]
                        return
                    return ["U"]
                if node.val ==destValue:
                    if left:
                        self.ans = [left]
                        return 
                    if right:
                        self.ans = [right]
                    return [dr]
                
                if left and right:
                    self.ans = [left,right]
                    return
                if left:
                    if left[-1] == "U": left.append("U")
                    else: left.append(dr)
                    return left
                if right:
                    if right[-1] == "U": right.append("U")
                    else: right.append(dr)
                    return right
                
        
        
        dfs(root,"")
        if len(self.ans)== 2:
            if self.ans[0][-1] == "U": return "".join(self.ans[0]+ self.ans[1][::-1])
            return "".join(self.ans[1] + self.ans[0][::-1])
        else:
            if self.ans[0][-1] == "U": self.ans[0].reverse()
            return "".join(self.ans[0])
