class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        chars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
       
        change = defaultdict(int)
        for shift in shifts:
            if shift[2] == 0:
                change[shift[0]] -= 1
                change[shift[1]+ 1] += 1
            else:
                change[shift[0]] += 1
                change[shift[1] + 1] -= 1
                
        shift = 0
        ans = []
        for ind  in range(len(s)):
            shift += change[ind]
            ans.append(chars[(ord(s[ind])-97 + shift)%26])
            
        return "".join(ans)