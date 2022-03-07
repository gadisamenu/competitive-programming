class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        lgth = len(beginWord)
        pattern_matchs = defaultdict(list)
        visited = set()
        for word in wordList:
            for i in range(lgth):
                pattern = word[:i]+"*"+word[i+1:]
                pattern_matchs[pattern].append(word)
                             
    
        que= deque([(beginWord,1)])
        visited.add(beginWord)
        while que:
            cur = que.popleft()
            
            if cur[0] == endWord:
                return cur[1]
            for  i in range(lgth):
                pattern = cur[0][:i]+"*"+cur[0][i+1:]
                for word in pattern_matchs[pattern]:
                    if word not in visited:
                        visited.add(word)
                        que.append((word,cur[1]+1))
                pattern_matchs.pop(pattern)
        return 0
             
        