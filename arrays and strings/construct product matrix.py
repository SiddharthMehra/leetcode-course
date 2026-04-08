class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:

        mod = 12345

        m, n = len(grid), len(grid[0])

        #flatten grid
        arr = []
        for row in grid:
            arr.extend(row)
        
        size = m * n

        #prefix
        prefix = [1] * size
        for i in range(1, size):
            prefix[i] = (prefix[i-1] * arr[i-1]) % mod
        
        #suffix
        suffix = [1] * size
        for i in range(size-2, -1, -1):
            suffix[i] = (suffix[i+1] * arr[i+1]) % mod
        
        #result
        result = [0] * size
        for i in range(size):
            result[i] = (prefix[i] * suffix[i]) % mod
        
        #reshape back to grid
        res = []
        idx = 0
        for i in range(m):
            row = []
            for j in range(n):
                row.append(result[idx])
                idx+=1

            res.append(row)
        
        return res
        

        

        
