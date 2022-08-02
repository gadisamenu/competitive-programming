class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        ans = defaultdict(list)
        i = len(num1) -1
        for n in num1:
            n = int(n)
            for m in num2:
                ans[i].append(n* int(m))
            i -= 1
            
        s = deque()
        
        for n in ans:
            for i in range(1,len(ans[n])+1):
                
                while -1*(-i-n) > len(s):
                    s.appendleft(0)
                                  
                s[-n-i] += ans[n][-i]
                
        kep = 0
        
        for n in range(1,len(s)+1):
            s[-n] += kep
            if s[-n]  > 9:
                kep = s[-n]// 10
                s[-n] %= 10
            else:
                kep = 0
            s[-n] = str(s[-n])
            
        if kep > 0:
            s.appendleft(str(kep))
            
        if s[0] == "0":
            return "0"
            
        return  "".join(s)
     

                
