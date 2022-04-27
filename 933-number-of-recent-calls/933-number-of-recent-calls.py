class RecentCounter:

    def __init__(self):
        self.start =0
        self.requests = []
    def ping(self, t: int) -> int:
        self.requests.append(t)
        while  self.requests[-1] - self.requests[self.start] > 3000:
            self.start+=1
        return len(self.requests) - self.start
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)