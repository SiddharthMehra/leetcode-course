class Solution:       
    def cleanRoom(self, robot):

        directions = [(-1, 0),(0,-1),(1,0),(0,1)]
        visited = set()

        def go_back():
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()
        
        def backtrack(x, y, direction):
            visited.add((x, y))
            robot.clean()

            for i in range(4):
                new_direction = (direction+i) % 4
                new_x = x + directions[new_direction][0]
                new_y = y + directions[new_direction][1]

                if (new_x, new_y) not in visited and robot.move():
                    backtrack(new_x, new_y, new_direction)
                    go_back()
                
                robot.turnRight()
            
        backtrack(0, 0, 0)
