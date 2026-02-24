class Solution:
    def bowlSubarrays(self, nums: List[int]) -> int:

        stack = []
        ans = 0

        for num in nums:
            #monotonically decreasing
            while stack and stack[-1]<num:
                stack.pop()
                if stack:
                    ans+=1
            stack.append(num)
        
        return ans
        
