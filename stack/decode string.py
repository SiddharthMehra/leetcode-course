class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        for i in range(len(s)):
            #only pop when closing bracket
            if s[i]!="]":
                stack.append(s[i])
            else:
                #pop the character(s)
                substr = ""
                while stack[-1]!='[':
                    substr = stack.pop() + substr
                stack.pop()

                #pop the number of times the character(s) appear
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                
                stack.append(int(k) * substr)
            
        return "".join(stack)

        

