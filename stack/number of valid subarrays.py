# valid subarrays where first element is the smallest

class Solution:
    def validSubarrays(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for num in nums:
            while stack and stack[-1]>num:
                stack.pop()

            stack.append(num)
            ans+=len(stack)

        return ans        