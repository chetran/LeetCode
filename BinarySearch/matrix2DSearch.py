from utils import checker

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r  = 0, len(nums) - 1 
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    checker(solution.search(nums = [-1,0,2,4,6,8], target = 4), 3)
    checker(solution.search(nums = [-1,0,2,4,6,8], target = 3), -1)

