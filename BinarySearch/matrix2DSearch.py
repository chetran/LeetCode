from utils import checker

class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        l, r  = 0, len(nums) - 1 
        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] == target:
                return True
            if nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        l, u = 0, len(matrix) - 1 
        while l <= u:
            mid = l + (u - l) // 2 
            if target >= matrix[mid][0] and target <= matrix[mid][-1]:
                return self.search(matrix[mid], target)
            if target < matrix[mid][0]:
                u = mid - 1
            else:
                l = mid + 1 
        return False


if __name__ == '__main__':
    solution = Solution()
    checker(solution.search(nums = [-1,0,2,4,6,8], target = 4), True)
    checker(solution.search(nums = [-1,0,2,4,6,8], target = 3), False)

    checker(solution.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 10), True)
    checker(solution.searchMatrix(matrix = [[1,2,4,8],[10,11,12,13],[14,20,30,40]], target = 15), False)
    checker(solution.searchMatrix(matrix=[[1,3,5,7],[10,11,16,20],[23,30,34,60]], target=3), True)
