import heapq

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        n = len(profits)
        projects = list(zip(capital, profits))
        projects.sort()

        q = []
        idx = 0

        for i in range(k):
            while idx<n and projects[idx][0]<=w: #check if project capital is less than current capital
                heappush(q, -projects[idx][1]) #push the profit
                idx+=1
            #no project<capital
            if not q:
                break
            
            #add popped element profit to the capital
            w+= (-heappop(q))
        
        return w



