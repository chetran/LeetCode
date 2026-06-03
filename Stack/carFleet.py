from collections import deque

class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        cars = [(position[i], speed[i]) for i in range(len(position))]
        cars.sort(key=lambda x:x[0])
        s = deque() 
        for i in range(len(position)-1, -1, -1):
            if len(s) > 0:
                top = s[-1]
                tleft = (target - top[0]) / top[1]
                cleft = (target - cars[i][0]) / cars[i][1]
                print(tleft, cleft)
                if tleft < cleft:
                    s.append(cars[i])
                else:
                    print(top, cars[i])
            else: 
                s.append(cars[i])

        print(s)
        return len(s)

                

def checker(received, answer):
    if received != answer:
        print(f'FAILED: Received: {received}, but expected: {answer}.')
        return 
    print("PASSED!")

if __name__ == '__main__':
    solution = Solution()
    #checker(solution.carFleet(target = 10, position = [1,4], speed = [3,2]), 1)
    checker(solution.carFleet(target = 10, position = [4,1,0,7], speed = [2,2,1,1]), 3)
