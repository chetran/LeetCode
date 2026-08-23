#!/usr/bin/env python3

from utils import checker

class Solution:
    def checkDivisibility(self, n: int) -> bool:
        sums, prod, nums = 0, 1, n
        while nums > 0:
            d = nums % 10 
            nums //= 10
            sums += d
            prod *= d
        return n % (sums + prod) == 0

if __name__ == '__main__':
    solution = Solution()
    checker(solution.checkDivisibility(99), True)
    checker(solution.checkDivisibility(23), False)
