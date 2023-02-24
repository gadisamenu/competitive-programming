from sortedcontainers import SortedList
class TweetCounts:

    def __init__(self):
        self.tweets = defaultdict(SortedList)
        self.jump = {"minute":59,"hour":3599,"day":86399}

    def recordTweet(self, tweetName: str, time: int) -> None:
        self.tweets[tweetName].add(time)        
        

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        tweets = self.tweets[tweetName]
        answer = []
        start = bisect_left(tweets,startTime)
        while startTime <= endTime:
            startTime = min(endTime,startTime+self.jump[freq])
            
            end_index = bisect_right(tweets,startTime)
            answer.append(end_index-start)
            startTime+=1
            start = bisect_left(tweets,startTime)
        
        return answer
            
  


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)