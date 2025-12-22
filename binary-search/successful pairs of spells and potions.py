class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans = []
        m = len(potions)
        maxPotion = potions[m-1]

        for spell in spells:
            minPotion = math.ceil(success/spell)
            if minPotion>maxPotion:
                ans.append(0)
                continue
            idx = bisect_left(potions, minPotion)
            ans.append(m-idx)
        
        return ans

        
        
