from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        stack = deque()
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][0] < temperatures[i]:
                _, idx = stack.pop()
                res[idx] = i - idx
            stack.append((temperatures[i], i))
        
        return res
                

def checker(received, answer):
    if received != answer:
        print(f'FAILED: Received: {received}, but expected: {answer}.')
        return 
    print("PASSED!")

if __name__ == '__main__':
    solution = Solution()
    checker(solution.dailyTemperatures([30,38,30,36,35,40,28]), [1,4,1,2,1,0,0])
    checker(solution.dailyTemperatures([21,20,19]), [0,0,0])
