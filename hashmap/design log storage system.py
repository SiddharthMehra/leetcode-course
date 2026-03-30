class LogSystem:

    def __init__(self):

        self.storage = []
        
    def put(self, id: int, timestamp: str) -> None:

        self.storage.append((timestamp, id))

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:

        granularity2index = {"Year": 4, "Month": 7, "Day":10, "Hour": 13, "Minute": 16, "Second": 19}
        index = granularity2index[granularity]
        return [id for timestamp, id in self.storage if start[:index]<=timestamp[:index]<=end[:index]]
        


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)
