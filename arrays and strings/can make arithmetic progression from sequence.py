class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        min_value, max_value = min(arr), max(arr)

        n = len(arr)
        if (max_value - min_value) % (n-1):
            return False
        
        diff = (max_value - min_value) // (n-1)

        i=0
        while i<n:
            #if arr[i] is at correct index, move on
            if arr[i] == min_value + i * diff:
                i+=1
            
            elif (arr[i] - min_value) % diff:
                return False
            
            else:
                j = (arr[i] - min_value) // diff

                #duplicate elements
                if arr[i] == arr[j]:
                    return False
                
                arr[i], arr[j] = arr[j], arr[i]

        return True
                

                


        
