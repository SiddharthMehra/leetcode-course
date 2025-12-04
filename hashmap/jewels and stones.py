class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        
        count = Counter(stones)
        ans=0
        for key, value in Counter(jewels).items():
            if key in count:
                ans+=count[key]
                del count[key]
        
        return ans
                
            
        