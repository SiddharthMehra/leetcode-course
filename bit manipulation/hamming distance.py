class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

    #XOR outputs 1 only if the corresponding bits are different. So, in order to measure hamming distance between x and y just do x XOR y

        #using built in function
        # return bin(x^y).count('1')

        #brian kernighan's algorithm

        xor = x ^ y
        distance = 0
        while xor:
            distance+=1
            #each xor operation following removes the rightmost set '1' bit
            xor = xor & (xor-1)
        
        return distance
