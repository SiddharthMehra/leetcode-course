class Solution:
    def largestNumber(self, nums: List[int]) -> str:

        num_strings = [str(num) for num in nums]

        #multiply by 10 to normalise -> '3' * 10 = 3333333333, '30' * 10< '3" * 10
        num_strings.sort(key = lambda a: a*10, reverse = True)

        #sorted in descending order, so if first is 0, all are '0'
        if num_strings[0] == '0':
            return '0'
        
        return "".join(num_strings)
