class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        n = len(heights)
        maxarea = 0
        stack = []

        for i in range(n):
            #if smaller height than at top of the stack, extend towards the left
            while stack and heights[i]<heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i-stack[-1]-1
                maxarea = max(maxarea, height*width)
            
            stack.append(i)
        
        #for rest, rightmost boundary is n
        while stack:
            height = heights[stack.pop()]
            width = n if not stack else n-stack[-1]-1
            maxarea = max(maxarea, height*width)
        
        return maxarea

