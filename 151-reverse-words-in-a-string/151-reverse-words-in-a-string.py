class Solution:
    def reverseWords(self, s: str) -> str:
        lst_s = []
        s += " "
        srt = 0
        for ind in range(len(s)):
            if s[ind] == " " :
                if ind - srt: lst_s.append(s[srt:ind])
                srt = ind+1
        
        lst_s.reverse()
        return " ".join(lst_s)