class DetectSquares:

    def __init__(self):
        self.points = defaultdict(lambda: defaultdict(int))

    def add(self, point: List[int]) -> None:
        self.points[point[0]][point[1]] += 1

    def count(self, point: List[int]) -> int:
        count = 0
        for y in self.points[point[0]]:
            size = abs(y-point[1])
            if size == 0:
                continue
            count += self.points[point[0]][y]*self.points[(point[0]-size)][y]*self.points[(point[0]-size)][point[1]]
            count += self.points[point[0]][y]*self.points[(point[0]+size)][y]*self.points[(point[0]+size)][point[1]]
            
        return count
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)