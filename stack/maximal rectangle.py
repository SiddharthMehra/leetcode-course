#convert into histogram and use the result of largest rectangle histogram
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        maxarea = 0
        dp = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                dp[j] = dp[j] + 1 if matrix[i][j] == "1" else 0
            
            maxarea = max(maxarea, self.largestRectangleArea(dp))
        
        return maxarea

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




        
