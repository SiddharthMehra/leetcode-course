class Leaderboard:

    def __init__(self):
        self.scores = defaultdict()
    
    def addScore(self, playerId, score):
        if playerId not in self.scores:
            self.scores[playerId] = 0
        
        self.scores[playerId]+=score
    
    def top(self, K):
        
        #min heap by default in python
        heap = []

        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap)>K:
                heapq.heappop(heap)
        
        res = 0
        while heap:
            res+=heapq.heappop(heap)
        
        return res
       
    def reset(self, playerId):
        self.scores[playerId] = 0


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
