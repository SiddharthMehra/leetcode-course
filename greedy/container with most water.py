#two pointer

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxarea = 0
        left, right = 0, len(height)-1

        while left<right:
            width = right-left
            maxarea = max(maxarea, min(height[left], height[right]) * width)

            if height[left]<=height[right]:
                left+=1
            else:
                right-=1
        
        return maxarea
