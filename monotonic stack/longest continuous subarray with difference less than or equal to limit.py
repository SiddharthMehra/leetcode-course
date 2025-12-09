class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:

        increasing, decreasing = deque(), deque()
        left, ans = 0, 0

        for right in range(len(nums)):

            # maintain the increasing and decreasing variant respectively
            while increasing and increasing[-1]>nums[right]:
                increasing.pop()
            while decreasing and decreasing[-1]<nums[right]:
                decreasing.pop()

            increasing.append(nums[right])
            decreasing.append(nums[right]) 

            #shrink window if difference greater than limit
            #delete left if present in either queues
            while decreasing[0]-increasing[0]>limit:
                if nums[left]==decreasing[0]:
                    decreasing.popleft()
                
                if nums[left]==increasing[0]:
                    increasing.popleft()

                left+=1 
            
            ans = max(ans, right-left+1)
        
        return ans




