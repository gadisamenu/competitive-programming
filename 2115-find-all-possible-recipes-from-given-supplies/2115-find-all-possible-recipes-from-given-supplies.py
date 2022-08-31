class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        in_degree = defaultdict(int)
        graph = defaultdict(list)
        recipes_s = set(recipes)
        
        for ind in range(len(recipes)):
            in_degree[recipes[ind]] = len(ingredients[ind])
            for ingredient in ingredients[ind]:
                graph[ingredient].append(recipes[ind])
        
        que = deque(supplies)
        ans = []
        while que:
            cur = que.popleft()
            
            if cur in recipes_s:
                ans.append(cur)
                
            for ngh in graph[cur]:
                in_degree[ngh] -= 1
                if not  in_degree[ngh]:
                    que.append(ngh)
            
        return ans