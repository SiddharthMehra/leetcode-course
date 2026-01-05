class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        total = rows*cols
        res = [0]*total

        r, c = 0, 0

        for i in range(total):
            res[i] = matrix[r][c]
            
            #direction up right
            if (r+c)%2==0:
                #both if and elif cases boundary conditions, if end of up right go down left
                if c == cols-1:
                    r+=1
                elif r == 0:
                    c+=1
                #normal up right
                else:
                    r-=1
                    c+=1
            
            else:
                #moving down left
                if r == rows-1:
                    c+=1
                elif c == 0:
                    r+=1
                else:
                    r+=1
                    c-=1
        
        return res
