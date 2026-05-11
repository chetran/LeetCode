class Solution:
    def trap(self, height: list[int]) -> int:
        l, r, l_max, r_max = 0, len(height) - 1, height[0], height[len(height) - 1]
        
        res = 0 
        while l <= r:
            if l_max < r_max:
                diff = l_max - height[l]
                if diff < 0:
                    diff = 0
                    l_max = height[l]
                res += diff
                l += 1
            else:
                diff = r_max - height[r]
                if diff < 0:
                    diff = 0
                    r_max = height[r]
                res += diff
                r -= 1
        return res


solution = Solution()
print(solution.trap(height = [0,2,0,3,1,0,1,3,2,1]) == 9)
print(solution.trap(height=[0,1,0,2,1,0,1,3,2,1,2,1]) == 6)

