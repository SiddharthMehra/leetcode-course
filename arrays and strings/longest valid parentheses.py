class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, max_length = 0, 0, 0
        #1. left to right -> to account for more ')'
        for i in range(len(s)):
            if s[i] == "(":
                left+=1
            else:
                right+=1

            #well formed parenthesis
            if left == right:
                max_length = max(max_length, 2*left)
            
            #reset
            elif right>left:
                left = right = 0
            
        left = right = 0
        #2. iterating in reverse to account for more '('
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left+=1
            else:
                right+=1
            
            if left == right:
                max_length = max(max_length, 2*left)
            
            elif left>right:
                left = right = 0
        
        return max_length
