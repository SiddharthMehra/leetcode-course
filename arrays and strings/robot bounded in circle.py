class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #facing north
        dirX, dirY = 0, 1
        x, y = 0, 0

        for d in instructions:
            if d == "G":
                x, y = x+dirX, y+dirY

            elif d == "L":
                dirX, dirY = -dirY, dirX
            
            else:
                dirX, dirY = dirY, -dirX
        
        #either it returns to origin or changes direction in 1 cycle
        return (x, y) == (0,0) or (dirX, dirY) != (0,1)



        
