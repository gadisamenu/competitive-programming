class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        if not stations:
            return -1 if target > startFuel else 0
        heap =[]
        sm = startFuel
        
        count = 0
        
        for ind in range(len(stations)):
            if stations[ind][0] <= sm:
                heappush(heap,-stations[ind][1])
            elif heap:
                while heap and stations[ind][0] > sm :
                    count+= 1
                    sm += - heappop(heap)
                if stations[ind][0] <= sm:
                    heappush(heap,-stations[ind][1])
            else:
                return -1
        while heap and target > sm:
            sm += - heappop(heap)
            count += 1
        return -1 if target > sm else count