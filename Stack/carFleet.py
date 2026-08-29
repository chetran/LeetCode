#!/usr/bin/env python3

from collections import deque

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: -x[0])
        s = []
        for c in cars:
            miles = (target - c[0]) / c[1]
            if not s or (s and miles > s[-1]):
                s.append(miles)
        return len(s)

def checker(received, answer):
    if received != answer:
        print(f'FAILED: Received: {received}, but expected: {answer}.')
        return 
    print("PASSED!")

if __name__ == '__main__':
    solution = Solution()
    checker(solution.carFleet(target = 10, position = [1,4], speed = [3,2]), 1)
    checker(solution.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]), 3)
