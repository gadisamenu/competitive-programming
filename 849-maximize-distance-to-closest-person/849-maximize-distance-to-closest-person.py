class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        _max = seats.index(1)
        strt = _max
        for i in range(_max,len(seats)):
            if seats[i] == 1:
                _max = max(_max,(i-strt)//2)
                strt = i
        _max = max(_max,len(seats)-1-strt)
        return _max
            