class Solution:
    def maxArea(self, heights: list[int]) -> int:
        l, r = 0, len(heights) - 1
        res = 0
        while l < r:
            smaller = min(heights[l], heights[r])
            area = (r-l) * smaller
            res = max(res, area)
            if smaller == heights[l]:
                l += 1
            else:
                r -= 1
        print(res)
        return res


solution = Solution()
print(solution.maxArea([1,7,2,5,4,7,3,6]) == 36)
print(solution.maxArea([2,2,2]) == 4)
print(solution.maxArea([1,7,2,5,12,3,500,500,7,8,4,7,3,6]) == 500)

