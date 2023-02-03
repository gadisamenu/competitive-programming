class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = defaultdict(list)
        repet = 2 *(numRows-1)
        numRows -= 1
          
        for n in range(len(s)):
            m = n % repet
            
            if m > numRows:
                rows[numRows-(m%numRows)].append(s[n])
                
            else: rows[m].append(s[n])
                
        ans = []
        for row in rows.values():
            ans+=row
     
            
        return ''.join(ans)
            
        