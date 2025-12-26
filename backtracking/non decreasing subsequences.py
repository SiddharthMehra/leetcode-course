class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        sequence = []

        def backtrack(index):
            if len(sequence)>=2:
                result.append(sequence[:])

            #to prevent duplicates at the same level
            used = set()
            for i in range(index, len(nums)):
                if nums[i] in used:
                    continue
                
                if not sequence or sequence[-1]<=nums[i]:
                    used.add(nums[i])
                    sequence.append(nums[i])
                    backtrack(i+1)
                    sequence.pop()
        backtrack(0)
        return result
