class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        heights = [0] * n
        res = 0

        #count consecutive ones at col j
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 1:
                    heights[j]+=1
                else:
                    heights[j] = 0
            stack = [[-1, 0, -1]]
            for i, h in enumerate(heights):
                #monotonic increasing stack
                while stack[-1][2]>=h:
                    stack.pop()
                
                #extend left boundary from i+1 to j-1 giving j-i possible positions
                j, prev, _ = stack[-1]
                curr = prev + (i-j) * h
                stack.append([i, curr, h])
                res+=curr
        
        return res

        
