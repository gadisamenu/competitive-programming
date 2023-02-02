class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letter_logs = []
        digit_logs = []
        
        for log in range(len(logs)):
            for idx in range(len(logs[log])):
                if logs[log][idx] == " ":
                    _id = logs[log][:idx]
                    body = logs[log][idx+1:]
                    if body[0].isdigit():
                        digit_logs.append(logs[log])
                    else:
                        letter_logs.append((body,_id,log))
                    break
                    
        letter_logs.sort()
        answer = []
        for log in letter_logs:
            answer.append(logs[log[2]])
        answer.extend(digit_logs)
        
        return answer
       
            
            