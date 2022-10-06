class TimeMap:

    def __init__(self):
        self.data = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.data[key].append((timestamp,value))
        
    def get(self, key: str, timestamp: int) -> str:
        if self.data[key]:
            ind = bisect_left(self.data[key],timestamp,key=lambda x:x[0])
            if ind >= len(self.data[key]): return self.data[key][-1][1]
            print(self.data[key][ind])
            if self.data[key][ind][0] > timestamp: 
                if ind == 0:return ""
                return self.data[key][ind-1][1]
            return self.data[key][ind][1]
        
        return ""
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)