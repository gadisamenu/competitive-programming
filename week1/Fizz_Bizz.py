class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans =[]
        for i in range(1,n+1):
            mod3 = i % 3 == 0
            mod5 = i % 5 == 0
            if mod3:
                if mod5:
                    ans.append('FizzBuzz')
                else:
                    ans.append('Fizz')
            elif mod5:
                ans.append('Buzz')
            else:
                ans.append(str(i))
                
        return ans