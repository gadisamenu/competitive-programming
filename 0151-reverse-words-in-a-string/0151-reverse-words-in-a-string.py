class Solution:
    def reverseWords(self, s: str) -> str:
        answer = []
        pre=" "
        for c in s:
            if c != " ":
                if pre == " ":
                    answer.append([])
                answer[-1].append(c)     
            pre = c
            
        for i in range(len(answer)):
            answer[i] = "".join(answer[i])

        return " ".join(answer[::-1])
    
    
        
                
                
    