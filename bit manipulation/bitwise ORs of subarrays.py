class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        seen, curr = set(), set()

        for num in arr:
            new_curr = {num}
            for x in curr:
                new_curr.add(x | num)
            
            curr = new_curr
            seen |= curr
        
        return len(seen)
