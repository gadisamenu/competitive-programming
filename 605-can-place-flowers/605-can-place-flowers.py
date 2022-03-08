class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        lgth = len(flowerbed)
        i = 0
        while i < lgth:
            if flowerbed[i] == 0 and (i == lgth-1 or flowerbed[i+1] != 1):
                n-=1
                i+=2
            elif flowerbed[i]==1:
                i+=2
            else:
                i+=3
        return True if n < 1 else False
        