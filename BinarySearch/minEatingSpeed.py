from utils import checker
import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r = 0, max(piles)
        res = r
        while l <= r:
            m = l + (r - l) // 2
            passed_time = 0
            for i in piles:
                if m == 0:
                    passed_time = h + 1
                    break
                passed_time += math.ceil(i / m)
            if passed_time > h:
                l = m + 1  
            else:
                res = m
                r = m - 1  
        return res

if __name__ == '__main__':
    solution = Solution()
    checker(solution.minEatingSpeed(piles = [1,4,3,2], h = 9), 2)
    checker(solution.minEatingSpeed(piles = [25,10,23,4], h = 4), 25)
