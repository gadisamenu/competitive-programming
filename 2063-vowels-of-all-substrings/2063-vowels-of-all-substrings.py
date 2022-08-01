class Solution:
    def countVowels(self, word: str) -> int:
        n_vowels = 0
        
        vowels = {'a','e','i','o','u'}
        lgth = len(word)
        for idx in range(lgth):
            if word[idx] in vowels:
                n_vowels += (idx+1)*(lgth - idx)
                
        return n_vowels
        