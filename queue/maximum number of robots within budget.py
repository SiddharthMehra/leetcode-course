class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:

        n = len(chargeTimes)
        max_deque = deque()
        current_sum = 0

        left, ans = 0, 0

        for right in range(n):

            while max_deque and chargeTimes[max_deque[-1]]<=chargeTimes[right]: #monotonically decreasing queue, maintain 
                max_deque.pop()
            
            max_deque.append(right)
            current_sum+=runningCosts[right]

            #shrink from the left
            while max_deque and (chargeTimes[max_deque[0]] + (right-left+1) * current_sum)>budget:
                if max_deque[0] == left:
                    max_deque.popleft()
                current_sum-=runningCosts[left]
                left+=1
        
            ans = max(ans, right-left+1)
    
        return ans



