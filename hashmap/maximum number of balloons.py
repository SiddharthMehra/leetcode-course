class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        pattern_str = "balloon"
        countPattern = Counter(pattern_str)
        minValue = float('inf')
        for char in pattern_str:
                minValue = min(minValue, count[char]//countPattern[char])
        
        return minValue if minValue!=float('inf') else 0
            
        