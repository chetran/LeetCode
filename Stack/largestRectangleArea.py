from utils import checker

class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        s = []
        res = 0 
        for i, h in enumerate(heights):
            newidx = i
            while len(s) > 0 and s[-1][1] > h:
                top = s.pop()
                res = max(top[1] * (i - top[0]), res)
                newidx = top[0]
            i = newidx
            s.append((i, h))

        for i, h in s:
            res = max(h * (len(heights) - i), res)
        return res 

if __name__ == '__main__':
    solution = Solution()
    checker(solution.largestRectangleArea(heights = [7,1,7,2,2,4]), 8)
    checker(solution.largestRectangleArea(heights = [1,3,7]), 7)
    #checker(solution.largestRectangleArea(), )
