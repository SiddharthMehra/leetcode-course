class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = defaultdict(int)

        max_frequency = 0
        ans = 0

        for num in nums:
            freq[num]+=1
            frequency = freq[num]

            if frequency>max_frequency:
                max_frequency = frequency
                ans = frequency
            
            elif frequency == max_frequency:
                ans+=frequency
        
        return ans

