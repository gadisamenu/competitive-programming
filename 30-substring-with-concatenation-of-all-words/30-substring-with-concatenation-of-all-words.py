class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
              
        s_words = set(words)
        count = Counter(words)
        triples = defaultdict(str)
        w_lg = len(words[0])
        i = 0
        j = w_lg-1
        while j < len(s):
            if s[i:j+1] in s_words:
                triples[i]  = s[i:j+1]
            i+=1
            j+=1
            
        indexs = list(triples.keys())
        ans =[]
        i =0
        while i < len(indexs):
            if indexs[i] in triples:
                n_count = defaultdict(int)
                ans.append(indexs[i])
                done = len(words)
                stack = [indexs[i]]
                while stack:
                    ind = stack.pop()
                    n = triples[ind]
                    if n_count[n] < count[n]:
                        n_count[n] += 1
                        done -= 1
                        if not done: break
                    else:
                        ans.pop()
                        break
                    if (ind + w_lg) in triples:
                        stack.append(ind+w_lg)
                    else:
                        ans.pop()
                        break
                    
            i+=1
        return ans
                    
            