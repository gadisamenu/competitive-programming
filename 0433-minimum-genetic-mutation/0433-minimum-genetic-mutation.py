class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        """
        4*8
        """
        move = {1:"A",2:"C",3:"T",0:"G"}
        
        bank = set(bank)
        visited = {start}
        queue = deque([start])
        mutations = 0
        while queue:
            lgth = len(queue)
            while lgth:
                gene = queue.popleft()
                if gene == end:
                    return mutations
                _next = list(gene)

                for i in range(len(_next)):
                    for j in range(4):
                        if gene[i] != move[j]:
                            _next[i] = move[j]
                            mutant = "".join(_next)
                            if mutant in bank and mutant not in visited:
                                queue.append(mutant)
                                visited.add(mutant)
                                
                    _next[i] = gene[i]
                                
                lgth -= 1

            mutations += 1            
                
        return -1
                