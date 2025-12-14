#bfs without modifying the input

from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid):
        rows, cols = len(grid), len(grid[0])

        if grid[0][0] != 0 or grid[rows-1][cols-1] != 0:
            return -1

        directions = [
            (-1,-1), (-1,0), (-1,1),
            (0,-1),          (0,1),
            (1,-1),  (1,0),  (1,1)
        ]

        current_layer = [(0,0)]
        visited = {(0, 0)}
        distance = 1
        next_layer = []

        while current_layer:
            for row, col in current_layer:

                if (row, col) == (rows-1, cols-1):
                    return distance

                for dr, dc in directions:
                    new_row, new_col = row + dr, col + dc
                    if (
                        0 <= new_row < rows and
                        0 <= new_col < cols and
                        (new_row, new_col) not in visited and
                        grid[new_row][new_col] == 0
                    ):
                        visited.add((new_row, new_col))
                        next_layer.append((new_row, new_col))
                
            distance+=1
            current_layer = next_layer
            next_layer = []

        return -1
