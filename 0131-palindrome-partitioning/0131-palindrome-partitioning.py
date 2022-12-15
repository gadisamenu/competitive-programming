class Solution:
    def partition(self, s: str) -> List[List[str]]:
        answer = []       
        
        """
        a a a b a a d e
        
        a a a b a a d e
        

        """
        def check(start,end):
            while start < end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True
        def count_answer(path):
            cur_answer = []
            for pair in path:
                cur_answer.append(s[pair[0]:pair[1]+1])
            answer.append(cur_answer)
        
        path = []
    
        def dp(start,end):
            if start  == len(s):
                count_answer(path)
            else:
                while end < len(s):
                    if check(start,end):
                        path.append((start,end))
                        dp(end+1,end+1)
                        path.pop()
                    end +=1 
                        
                    
        dp(0,0)
        return answer
            
        
        
        