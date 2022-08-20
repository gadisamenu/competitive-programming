class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        lgth = len(stations)
        heap =[]
        count = 0
        ind = 0
        while startFuel < target:
            while ind < lgth and startFuel >= stations[ind][0]:
                heappush(heap,-stations[ind][1])
                ind += 1
                
            if heap:
                count+= 1
                startFuel += - heappop(heap)
            else:
                return -1
            
        return count