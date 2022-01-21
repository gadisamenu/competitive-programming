class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pop = 0
        pushes=[]
        num = 0
        while num < len(pushed):
            if pushes and pushes[-1] == popped[pop]:
                pushes.pop()
                pop +=1
                            
            elif pushed[num] == popped[pop]:
                pop +=1
                num +=1
                
            else:
                pushes.append(pushed[num])
                num +=1
                            
            
            
        if pop < len(popped) and pushes:
             while pushes:
                if pushes.pop() ==popped[pop]:
                    pop +=1
                else:
                    return False
            
        if pushes:
            return False
        return True
                
    
        
            