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
            if self.tweets[id]:
                idx = len(self.tweets[id])-1
                lst.append((self.tweets[id][idx][0], self.tweets[id][idx][1], idx-1, id))
        
        if self.tweets[userId]:
            idx = len(self.tweets[userId])-1
            lst.append((self.tweets[userId][idx][0], self.tweets[userId][idx][1], idx-1, userId))
        
        heapq.heapify(lst)
        
        count = 0
        res = []
        
        while lst and count < 10:
            timer, tweetId, nxtIdx, id = heapq.heappop(lst)
            
            res.append(tweetId)
            count+=1
            
            if nxtIdx >= 0:
                heapq.heappush(lst,(self.tweets[id][nxtIdx][0], self.tweets[id][nxtIdx][1], nxtIdx-1, id))
        
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