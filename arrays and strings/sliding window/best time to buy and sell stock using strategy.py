class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)

        base = sum(strategy[i] * prices[i] for i in range(n))

        half = k//2

        gain_first = [0]*n
        gain_second = [0]*n

        for i in range(n):
            gain_first[i] = -strategy[i] * prices[i]
            gain_second[i] = prices[i] - prices[i] * strategy[i]
        
        curr_first = sum(gain_first[:half])
        curr_second = sum(gain_second[half:k])

        max_gain = 0

        max_gain = max(max_gain, curr_first + curr_second)

        for start in range(1, n-k+1):
            
            #remove from left
            curr_first-=gain_first[start-1]
            curr_second-=gain_second[start+half-1]

            #add from right
            curr_first+=gain_first[start+half-1]
            curr_second+=gain_second[start+k-1]

            max_gain = max(max_gain, curr_first + curr_second)
        
        return base + max_gain
        
