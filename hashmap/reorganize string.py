from collections import Counter
class Solution:
    def reorganizeString(self, s: str) -> str:

        freq = Counter(s)

        max_heap = [(-cnt, char) for char, cnt in freq.items()]
        heapq.heapify(max_heap)

        result = []

        while len(max_heap)>1:
            #take out the 2 most frequent characters
            count1, char1 = heapq.heappop(max_heap)
            count2, char2 = heapq.heappop(max_heap)

            result.append(char1)
            result.append(char2)

            #max_heap so count is negative
            if count1<-1:
                heapq.heappush(max_heap, (count1+1, char1))
            
            if count2<-1:
                heapq.heappush(max_heap, (count2+1, char2))
        
        #if only 1 character remains
        if max_heap:
            count, char = heapq.heappop(max_heap)
            #multiple counts of last char left, so not possible, else append to char
            if count <-1:
                return ""
            
            result.append(char)
        
        return "".join(result)


        

            





        
