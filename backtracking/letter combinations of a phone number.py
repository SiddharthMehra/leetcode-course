class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        
        hashmap ={
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        
        def backtrack(i, curr):
            if len(curr) == len(digits):
                ans.append("".join(curr))
                return
            
            for c in hashmap[digits[i]]:
                curr.append(c)
                backtrack(i+1, curr)
                curr.pop()
        
        ans = []
        backtrack(0, [])
        return ans
        
