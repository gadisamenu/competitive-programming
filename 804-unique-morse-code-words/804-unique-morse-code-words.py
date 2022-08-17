class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        maps = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        codes = set()
        
        for word in words:
            ptn = []
            for ch in word:
                ptn.append(maps[ord(ch)-97])
            codes.add("".join(ptn))
        return len(codes)