class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        answer = []
        
        line = []
        space = maxWidth
        for i in range(len(words)):
            if space < len(words[i]):
                space += len(line)
                gap = len(line)-1
                if gap:
                    put = ceil(space/gap)
                    rem = space%gap
                    x_space = " "*put
                    if rem:
                        f_half = x_space.join(line[:rem+1])
                        x_space = x_space[:-1]
                        s_half = x_space.join(line[rem+1:])
                        answer.append(f_half + x_space + s_half)
                    else:
                        answer.append(x_space.join(line))
    
                else:
                    answer.append(line[0]+" "*space)
                    
                    
                line= []
                space = maxWidth
        
            line.append(words[i])
            space -= (len(words[i]) +1)
        
        answer.append(" ".join(line) + " "*(space+1))
        
        return answer
            
            