class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:

        res = [0]*len(heights)
        stack = []

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]]<=height: # if taller in front. increase visibility and pop
                res[stack.pop()]+=1
            if stack:
                res[stack[-1]]+=1 # if not, just increase visibility by 1
        
            stack.append(i)
        
        return res
        