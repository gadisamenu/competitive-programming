class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        in_degree = defaultdict(int)
        for edge in edges:
            in_degree[edge[1]] += 1
        answer = []
        for  i in range(n):
            if in_degree[i] == 0:
                answer.append(i)
        return answer
            