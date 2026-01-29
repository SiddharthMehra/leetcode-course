class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        #go backwards from target to startValue
        operations = 0

        while target>startValue:
            operations+=1
            if target%2:
                target+=1
            else:
                target//=2
        
        #if you overshoot startValue
        operations+=(startValue - target)

        return operations
