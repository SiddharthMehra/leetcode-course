class MovingAverage:

    def __init__(self, size: int):
        self.max = size
        self.q = deque()
        self.total=0
        

    def next(self, val: int) -> float:
        
        self.q.append(val)
        self.total+=val
        if len(self.q)>self.max:
            self.total-=self.q.popleft()
        
        return self.total/len(self.q)
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)