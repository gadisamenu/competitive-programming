class Solution:
    def addBinary(self, a: str, b: str) -> str:
        keep = False
        
        a = list(reversed(a))
        b = list(reversed(b))
        
        answer = deque()
        lgth = min(len(a),len(b))
        
        for i in range(lgth):
            if a[i] == "1" and b[i] == "1" and keep:
                answer.append("1")
            elif ( keep and a[i] == '1') or (keep and b[i] == '1') or (a[i] == '1' and b[i] == '1'):
                answer.append("0")
                keep = True
            elif keep or a[i] == '1' or b[i] == '1':
                answer.append("1")
                keep = False
            else:
                answer.append("0")
        

        if len(a) < len(b):
            index = len(a)
            while keep and index < len(b):
                if b[index] == '1':
                    answer.append("0")
                else:
                    answer.append("1")
                    keep = False
                index += 1
            answer.extend(b[index:])
        elif len(a) > len(b):
            index = len(b)
            while keep and index < len(a):
                if a[index] == '1':
                    answer.append("0")
                else:
                    answer.append("1")
                    keep = False
                index += 1
            answer.extend(a[index:])
        
        if keep:
            answer.append("1")
            
        return "".join(reversed(answer))
            
            
                
            