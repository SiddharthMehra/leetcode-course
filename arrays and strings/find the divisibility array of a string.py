class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        curr = 0 
        ans = []
        for ch in word:
            curr = (curr*10 + int(ch))%m

            if curr == 0:
                ans.append(1)
            
            else:
                ans.append(0)
        
        return ans
            
        
