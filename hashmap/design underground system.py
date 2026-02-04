class UndergroundSystem:

    def __init__(self):

        self.checkin = {} #id -> stationName, time
        self.travels = {} #(start station ,end station) -> [totalTime, tripCount]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:

        self.checkin[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:

        startStation, startTime = self.checkin.pop(id)
        timeTaken = t - startTime

        key = (startStation, stationName)
        #visiting station for the first time 
        if key not in self.travels:
            self.travels[key] = [0, 0]
        
        self.travels[key][0]+=timeTaken
        self.travels[key][1]+=1

    def getAverageTime(self, startStation: str, endStation: str) -> float:

        totalTime, count = self.travels[(startStation, endStation)]
        return totalTime/count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
