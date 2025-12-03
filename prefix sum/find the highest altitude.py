class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        total = 0
        ans = 0

        for g in gain:
            total+=g
            ans = max(ans, total)
        
        return ans