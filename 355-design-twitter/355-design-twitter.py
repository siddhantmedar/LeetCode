class Twitter:

    def __init__(self):
        self.tweets = defaultdict(list)
        self.followMap = defaultdict(set)
        self.timer = 0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((-1*self.timer, tweetId))
        self.timer+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        lst = []
        
        for id in self.followMap[userId]:
            lst.extend(self.tweets[id])
        
        lst.extend(self.tweets[userId])
        
        heapq.heapify(lst)
        
        count = 0
        res = []
        
        while lst and count < 10:
            item = heapq.heappop(lst)
            res.append(item[1])
            count+=1
        
        return res
    
    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)