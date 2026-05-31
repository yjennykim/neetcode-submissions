import heapq
from collections import defaultdict

class Tweet:
    def __init__(self, id, created, author):
        self.id = id
        self.created = created
        self.author = author
    
    def __lt__(self, other):
        return self.created < other.created

class Twitter:

    def __init__(self):
        self.followMap = defaultdict(set) # user -> list of following
        self.tweets = defaultdict(list) # user -> list of tweets
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append(Tweet(tweetId, self.time, userId))
        self.time -= 1 # python uses minHeap, smallest numbers = more recent

    def getNewsFeed(self, userId: int) -> List[int]:
        minHeap = []
        self.followMap[userId].add(userId)
        for followee in self.followMap[userId]:
            index = len(self.tweets[followee]) - 1 # last index = most recent, add next index to check
            if index >= 0:
                heapq.heappush(minHeap, [self.tweets[followee][index], index-1])
        
        feed = []
        while minHeap and len(feed) < 10:
            recentTweet, index = heapq.heappop(minHeap)
            feed.append(recentTweet.id)
            author = recentTweet.author
            # author has more tweets
            print("Index", index)
            if index >= 0:
                heapq.heappush(minHeap, [self.tweets[author][index], index-1])
        
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followMap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followMap and followeeId in self.followMap[followerId]:
            self.followMap[followerId].remove(followeeId)
