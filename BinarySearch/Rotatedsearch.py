from utils import checker

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binS(left : int, right: int) -> int:
            while left <= right:
                m = (left + right) // 2 
                if nums[m] == target:
                    return m
                if nums[m] > target:
                    right = m - 1
                else:
                    left = m + 1
            return -1
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2 
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
        return max(binS(0, l - 1), binS(l, len(nums) - 1))

if __name__ == '__main__':
    solution = Solution()
    checker(solution.search(nums = [3,4,5,6,1,2], target = 1), 4)
    #checker(solution.search(nums = [-1,0,2,4,6,8], target = 3), -1)
