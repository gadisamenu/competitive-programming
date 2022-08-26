class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        n = str(n)
        for m in permutations(n,len(n)):
            if m[0] != "0":
                valid = True
                for b in bin(int("".join(m)))[3:]:
                    if b == "1":
                        valid = False
                        continue
                if valid : return True
                
        return False
            