#!/usr/bin/env python3

from utils import checker
import math

class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        a, b = nums1, nums2
        if len(a) > len(b):
            a, b = b, a

        l, r = 0, len(a)
        total_len = len(a) + len(b)
        half_len = total_len // 2

        while True:
            i = (l + r) // 2
            j = half_len - i
            aleft = a[i - 1] if i > 0 else -math.inf
            aright = a[i] if i < len(a) else math.inf
            bleft = b[j - 1] if j > 0 else -math.inf
            bright = b[j] if j < len(b) else math.inf

            if aleft <= bright and bleft <= aright:
                if total_len % 2:
                    return min(aright, bright)
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1
            else:
                l = i + 1

if __name__ == '__main__':
    solution = Solution()
    checker(solution.findMedianSortedArrays(nums1 = [1,2], nums2 = [3]), 2.0)
    checker(solution.findMedianSortedArrays(nums1 = [1,3], nums2 = [2,4]), 2.5)
