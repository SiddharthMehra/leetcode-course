class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:

        def gain(p, t):
            return (p+1)/(t+1) - p/t
        
        max_heap = []
        #greedily pop max gain from heap
        for p,t in classes:
            heapq.heappush(max_heap, (-gain(p, t), p, t))
        
        for _ in range(extraStudents):
            _, p, t = heapq.heappop(max_heap)
            p+=1
            t+=1
            heapq.heappush(max_heap, (-gain(p, t), p, t))
        
        total_ratio = 0
        for _, p, t in max_heap:
            total_ratio+=p/t
        
        return total_ratio/len(classes)

        

        
