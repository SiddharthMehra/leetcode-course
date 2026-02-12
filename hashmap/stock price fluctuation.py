class StockPrice:

    def __init__(self):

        self.latest_time = 0
        self.timestamp_price_map = {}

        self.min_heap = []
        self.max_heap = []
    def update(self, timestamp: int, price: int) -> None:

        #update price at current timestamp
        self.timestamp_price_map[timestamp] = price
        self.latest_time = max(self.latest_time, timestamp)

        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))
        
    def current(self) -> int:

        return self.timestamp_price_map[self.latest_time]
        
    def maximum(self) -> int:

        price, timestamp = self.max_heap[0]

        #pop outdated from hashmap when price does not match with hashmap
        while -price!=self.timestamp_price_map[timestamp]:
            heappop(self.max_heap)
            price, timestamp = self.max_heap[0]
        
        return -price

    def minimum(self) -> int:

        price, timestamp = self.min_heap[0]

        while price!=self.timestamp_price_map[timestamp]:
            heappop(self.min_heap)
            price, timestamp = self.min_heap[0]
        
        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
