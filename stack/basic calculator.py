class Solution:
    def calculate(self, s: str) -> int:

        stack = []
        operand = 0
        res = 0
        sign = 1

        for ch in s:
            if ch.isdigit():
                operand = operand * 10 + int(ch)
            
            elif ch == '+':

                res+=sign * operand
                sign = 1
                operand = 0
            
            elif ch == '-':
                
                res+=sign * operand
                sign = -1
                operand = 0
            
            elif ch == '(':
                
                #push the calculated result and then the sign
                stack.append(res)
                stack.append(sign)

                #reset sign and operand
                sign = 1
                res = 0
            
            elif ch == ')':
                
                #evaluate expression to the left
                res+=sign * operand
                #sign before 
                res*= stack.pop()

                #add the previously calculated result
                res+=stack.pop()

                operand = 0
        
        return res+sign* operand



