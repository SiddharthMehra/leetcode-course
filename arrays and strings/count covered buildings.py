class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:

        min_col = defaultdict(lambda: float('inf'))
        max_col = defaultdict(lambda: float('-inf'))
        min_row = defaultdict(lambda: float('inf'))
        max_row = defaultdict(lambda: float('-inf'))

        #find min/ max row per row and column
        for x,y in buildings:
            min_col[x] = min(min_col[x], y)
            max_col[x] = max(max_col[x], y)
            min_row[y] = min(min_row[y], x)
            max_row[y] = max(max_row[y], x)
        
        covered = 0

        for x,y in buildings:
            if y>min_col[x] and y<max_col[x] and x>min_row[y] and x<max_row[y]:
                covered+=1
        
        return covered

        
