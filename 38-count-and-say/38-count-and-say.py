class Solution:
    def countAndSay(self, n: int) -> str:
        
        def say(n):
            if n == 1:
                return "1"
            resp = self.countAndSay(n-1)
            num = resp[0]
            count = 0
            say = []
            for n in resp:
                if num == n:
                    count += 1

                else:
                    say.extend([str(count),num])
                    num = n
                    count = 1
            say.extend([str(count),num])

            return say
            
        return "".join(say(n))
             