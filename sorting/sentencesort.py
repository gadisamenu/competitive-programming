class Solution:
    def sortSentence(self, s: str) -> str:
        listed_s=s.split(" ")
        length= len(listed_s)
        for i in range(1,length):
            ind = i
            for j in range(i-1,-1,-1):
                if listed_s[ind][-1] < listed_s[j][-1]:
                    listed_s[ind],listed_s[j] = listed_s[j],listed_s[ind]
                    ind -=1
                else:
                    break
        ans =''
        for word in listed_s:
             ans += " " + word[:-1]
        return ans.strip()