class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        
        ans = [0 for i in range(n)]
       
        def dfs(nd,pre):
            count = defaultdict(int)
            for _nxt in graph[nd]:
                if _nxt != pre:
                    cnt =dfs(_nxt,nd)
                    for k in cnt:
                        count[k] += cnt[k]
                        
            count[labels[nd]] +=1
            ans[nd] = count[labels[nd]]
            return count
            
        dfs(0,-1)
        return ans
            