class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:

        stack = []

        for num in nums:
            stack.append(num)

            while len(stack)>1:
                a = stack[-1]
                b = stack[-2]
                g = gcd(a, b)

                if g == 1:
                    break
                
                lcm = a * b // g
                stack.pop()
                stack.pop()
                stack.append(lcm)
            
        return stack
        
