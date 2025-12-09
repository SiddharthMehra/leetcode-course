#monotonically decreasing queue
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        ans = []
        q = deque()

        for i in range(len(nums)):

            while q and nums[i]>nums[q[-1]]: #monotonically decreasing queue
                q.pop()
            
            q.append(i)

            if q[0] + k == i: #current element is outside the window
                q.popleft()
            
            if i>=k-1:
                ans.append(nums[q[0]])
        
        return ans

            
            




