# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader(object):
#	 # Compares the sum of arr[l..r] with the sum of arr[x..y]
#	 # return 1 if sum(arr[l..r]) > sum(arr[x..y])
#	 # return 0 if sum(arr[l..r]) == sum(arr[x..y])
#	 # return -1 if sum(arr[l..r]) < sum(arr[x..y])
#    def compareSub(self, l: int, r: int, x: int, y: int) -> int:
#
#	 # Returns the length of the array
#    def length(self) -> int:
#


class Solution:
    def getIndex(self, reader: 'ArrayReader') -> int:
        left = 0
        length = reader.length()
        while length>1:
            length//=2
            #break array into two halves of equal number of numbers
            cmp = reader.compareSub(left, left+length-1, left+length, left + 2*length-1)

            #heavier element is beyond the two halves
            if cmp == 0:
                return left + 2*length
            
            #heavier element is in the right half
            if cmp<0:
                left+=length
            
            #length is halved on each iteration so if cmp>0, automatically we search only the left half
        
        return left
            
            
        
