class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        max_element_possible = max(trip[2] for trip in trips) + 1
        arr = [0]*(max_element_possible)

        # at fromPlace, passengers pop in, at toPlace, they leave
        for passenger, fromPlace, toPlace in trips:
            arr[fromPlace]+=passenger
            arr[toPlace]-=passenger
        
        #if at any point the number of passengers are greater than capacity, return False else True
        curr = 0
        for i in range(len(arr)):
            curr+=arr[i]
            if curr>capacity:
                return False
            
        return True


        
