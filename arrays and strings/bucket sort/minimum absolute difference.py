class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        #bucket sort
        min_val, max_val = min(arr), max(arr)
        size = max_val - min_val + 1
        bucket = [False] * size

        for num in arr:
            bucket[num-min_val] = True
        
        #find minimum difference
        prev = None
        min_diff = float("inf")

        for i in range(size):
            if bucket[i]:
                if prev is not None:
                    min_diff = min(min_diff, i-prev)
                
                prev = i
        
        #collect pairs
        result = []
        prev = None

        for i in range(size):
            if bucket[i]:
                if prev is not None and i-prev == min_diff:
                    result.append([prev + min_val, i + min_val])
                
                prev = i
        
        return result
        

        
