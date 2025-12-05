class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1

        for key, value in Counter(arr).items():
            if key == value:
                ans = max(ans, key)
        
        return ans

        