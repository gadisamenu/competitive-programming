class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance =[]
        for pair in points:
            distance.append([(pair[0]**2 +pair[1]**2)**0.5,pair])
        distance = sorted(distance, key= lambda dis:dis[0])
        for _ in range(k):
            distance[_]= distance[_][1]
        return distance[:k]