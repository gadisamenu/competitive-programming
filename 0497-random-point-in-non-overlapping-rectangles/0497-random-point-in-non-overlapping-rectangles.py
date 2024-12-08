class Solution:
    
    def __init__(self,rects:List[List[int]]):
        self.rects = rects
        self.prefix_sum = [0]
        
        points = lambda rect: (rect[2] -  rect[0] + 1) * (rect[3] - rect[1] + 1)
        
        for i in range(len(self.rects)):
            self.prefix_sum.append(self.prefix_sum[-1] + points(self.rects[i]))
    
    def pick(self) -> List[int]:
        point = random.randint(1,self.prefix_sum[-1])
        
        ith_box = bisect.bisect_left(self.prefix_sum,point)
        
        point -= self.prefix_sum[ith_box- 1]
        
        x1,y1,x2,y2 = self.rects[ith_box - 1]
        
        q,r = divmod(point,x2-x1+1)
        if r:
            return [x1 + r -1, y1 + q]
        return [x2, y1 + q-1]
        
        
        
          


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()