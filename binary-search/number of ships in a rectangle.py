# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea:
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point:
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution:
    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:

        #recurse on the four rectangles inside

        x1, y1 = bottomLeft.x, bottomLeft.y
        x2, y2 = topRight.x, topRight.y

        if x1>x2 or y1>y2:
            return 0
        
        if not sea.hasShips( topRight, bottomLeft):
            return 0
        
        #single point, then one ship
        if x1==x2 and y1==y2:
            return 1
        
        midX = (x1+x2)//2
        midY = (y1+y2)//2

        return (
    self.countShips(sea, Point(midX, midY), Point(x1, y1)) +
    self.countShips(sea, Point(x2, midY), Point(midX + 1, y1)) +
    self.countShips(sea, Point(midX, y2), Point(x1, midY + 1)) +
    self.countShips(sea, Point(x2, y2), Point(midX + 1, midY + 1))
)
        


