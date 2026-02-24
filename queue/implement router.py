class Router:

    def __init__(self, memoryLimit: int):

        self.size = memoryLimit
        self.packets = {} #key -> [source, destination, timestamp]
        self.counts = defaultdict(list) #destination -> sorted list of timestamps
        self.q = deque() #FIFO order of packets
        

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:

        key = (source, destination, timestamp)

        if key in self.packets:
            return False
        
        #if memory full, forward oldest packet
        if len(self.packets)>=self.size:
            self.forwardPacket()
        
        self.packets[key] = [source, destination, timestamp]
        self.q.append(key)
        self.counts[destination].append(timestamp)

        return True
    
    def forwardPacket(self):
        if not self.packets:
            return []
        
        key = self.q.popleft()
        packet = self.packets.pop(key)
        dest = packet[1]
        #remove the earliest timestamp
        self.counts[dest].pop(0)

        return packet
    
    def getCount(self, destination, startTime, endTime):
        timestamps = self.counts.get(destination, [])

        if not timestamps:
            return 0
        
        left = bisect.bisect_left(timestamps, startTime)
        right = bisect.bisect_right(timestamps, endTime)

        return right - left

    
        


# Your Router object will be instantiated and called as such:
# obj = Router(memoryLimit)
# param_1 = obj.addPacket(source,destination,timestamp)
# param_2 = obj.forwardPacket()
# param_3 = obj.getCount(destination,startTime,endTime)
