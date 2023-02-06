class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        group = defaultdict(list)
        for word in words:
            group[len(word)].append([word,1])
            
        lgths = sorted(group,reverse = True)
        answer = 1
        for lgth in lgths:
            if lgth -1 in group:
                for word in group[lgth]:
                    answer = max(answer,self.compare(word,group))
        return answer 
    
    
    def compare(self,word,group):
        answer = word[1]
        lgth = len(word[0])-1
        for pred in group[lgth]:
            valid = True
            used = False
            j = 0
            for i in range(len(word[0])):
                if j < len(pred[0]):
                    if word[0][i] !=  pred[0][j]:
                        if used:
                            valid = False
                            break
                        used = True
                    else:                  
                        j += 1
                        
                elif used:
                    valid = False
                    
            
            if valid:
                pred[1]= max(pred[1],word[1]+1)
                answer = max(answer,pred[1])
            
        return answer
        
        