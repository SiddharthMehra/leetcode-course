class Solution:
    def nearestPalindromic(self, n: str) -> str:

        len_n = len(n)
        is_even = len_n %2==0

        mid = len_n//2 -1 if is_even else len_n//2

        first_half = int(n[:mid+1])

        possible_solutions = []

        possible_solutions.append(self.half_to_palindrome(first_half, is_even))

        possible_solutions.append(self.half_to_palindrome(first_half+1, is_even))

        possible_solutions.append(self.half_to_palindrome(first_half - 1, is_even))

        possible_solutions.append(10 ** len_n - 1)

        possible_solutions.append(10 ** len_n + 1)

        diff = float('inf')
        res = 0
        n_int = int(n)

        for candidate in possible_solutions:
            if candidate == n_int:
                continue

            if abs(candidate - n_int) < diff:
                diff = abs(candidate - n_int)
                res = candidate
            elif abs(candidate - n_int) == diff:
                res = min(res, candidate)

            return str(res)

        def half_to_palindrome(self, num, is_even):
            res = num

            if not is_even:
                num = num//10

            while num>0:
                res = res*10 + num % 10

                num//=10

            return res 

