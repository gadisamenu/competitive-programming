class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        for i in range(len(capital)):
            capital[i] = [capital[i],profits[i]]

        capital.sort()
        heap = [0]
        index = 0
       
        while heap and k:
            while index < len(capital) and capital[index][0] <= w:
                heappush(heap,-capital[index][1])
                index += 1
            w -= heappop(heap)
            k -= 1
     
        return w