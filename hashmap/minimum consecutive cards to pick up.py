class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left = 0
        ans = float('inf')
        hashmap = defaultdict(int)

        for i, card in enumerate(cards):
            if card in hashmap:
                ans = min(ans, i-hashmap[card]+1)
            
            hashmap[card]=i
        
        return ans if ans!=float('inf') else -1

