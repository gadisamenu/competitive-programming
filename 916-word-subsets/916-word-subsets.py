class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        chars_in_words2 = defaultdict(int)
        
        for word in words2:
            num_char = Counter(word)
            
            for ch in num_char:
                chars_in_words2[ch] = max(num_char[ch],chars_in_words2[ch])
                
        ans = []     
        for word in words1:
            num_char = Counter(word)
            valid=True
            for ch in chars_in_words2:
                if chars_in_words2[ch] > num_char[ch]:
                    valid = False
                    break
            if valid:ans.append(word)
        return ans
                
            
            