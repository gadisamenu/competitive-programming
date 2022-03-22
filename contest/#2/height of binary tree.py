def height(root):
    def dfs(node,dpth):
        left =dfs(node.left,dpth+1) if node.left else 0
        right =  dfs(node.right,dpth+1)if node.right  else 0
        return max(left,right,dpth)
    return dfs(root,0)