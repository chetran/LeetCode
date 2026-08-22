class Solution:
    def search(self, nums: list[int], target: int) -> int:
        def binSearch(left : int, right: int) -> int:
            mid = left + ((right - left) // 2)
            midVal = nums[mid]
            if midVal == target:
                return (mid)
            if right - left < 1:
                return -1
            if midVal > target:
                return binSearch(left, mid - 1)
            else:
                return binSearch(mid + 1, right)
        return binSearch(0, len(nums) - 1)

def checker(received, answer):
    if received != answer:
        print(f'FAILED: Received: {received}, but expected: {answer}.')
        return 
    print("PASSED!")

if __name__ == '__main__':
    solution = Solution()
    checker(solution.search(nums = [-1,0,2,4,6,8], target = 4), 3)
    checker(solution.search(nums = [-1,0,2,4,6,8], target = 3), -1)
