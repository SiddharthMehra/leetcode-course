class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts, ends = [], []

        for start, end in flowers:
            starts.append(start)
            ends.append(end+1) #flowers stop blooming at end+1
        
        starts.sort()
        ends.sort()
        ans = []

        for person in people:
            #no of flowers started blooming
            i = bisect_right(starts, person)
            #no of flowers ended blooming
            j = bisect_right(ends, person)
            ans.append(i-j)
        
        return ans


        
