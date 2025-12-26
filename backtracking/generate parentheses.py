class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(curr,left_count, right_count):
            if len(curr) == 2*n:
                ans.append("".join(curr))
                return 
            
            if left_count<n:
                curr.append("(")
                backtrack(curr, left_count+1, right_count)
                curr.pop()
            
            if right_count<left_count:
                curr.append(")")
                backtrack(curr, left_count, right_count+1)
                curr.pop()

        ans=[]
        backtrack([], 0, 0)
        return ans

        
