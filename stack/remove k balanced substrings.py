class Solution:
    def removeSubstring(self, s: str, k: int) -> str:

        stack = []

        for c in s:

            if stack and stack[-1][0] == c:
                stack[-1][1]+=1
            
            else:
                stack.append([c, 1])
            
            n = len(stack)
            if n>=2 and stack[n-2][0] == '(' and stack[n-2][1]>=k and stack[n-1][0] == ')' and stack[n-1][1] == k:
                stack[n-2][1]-=k
                stack.pop()
                if stack[-1][1] == 0:
                    stack.pop()
        
        result = ""
        for char, count in stack:
            result+=char*count
        
        return result

        
