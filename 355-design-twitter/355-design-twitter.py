class Twitter:
    
    def __init__(self):
        self.count = 10000
        self.twittes = defaultdict(deque)
        self.follows = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.follows[userId]: self.follows[userId].add(userId)
        self.twittes[userId].appendleft((self.count,tweetId))
        self.count -=1 
        

    def getNewsFeed(self, userId: int) -> List[int]:
        index = defaultdict(int)
        ans = []
        while len(ans) < 10:
            rcnt = 0
            for user in self.follows[userId]:
                if index[user] < len(self.twittes[user]):
                    if rcnt:
                        if self.twittes[rcnt][index[rcnt]][0] >  self.twittes[user][index[user]][0]: rcnt = user
                    else: rcnt= user
                    
            if not rcnt:break
            ans.append(self.twittes[rcnt][index[rcnt]][1])
            index[rcnt]+=1
                
        return ans
        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)
        
    
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]: self.follows[followerId].remove(followeeId)
    
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)