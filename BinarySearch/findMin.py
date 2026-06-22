from utils import checker

class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r - l) // 2
            if nums[m] <= nums[-1]:
                r = m - 1
            else:
                l = m + 1
        return nums[l]

if __name__ == '__main__':
    solution = Solution()
    checker(solution.findMin(nums = [3,4,5,6,1,2]), 1)
    checker(solution.findMin(nums = [4,5,0,1,2,3]), 0)
    checker(solution.findMin(nums = [4,5,6,7]), 4)
