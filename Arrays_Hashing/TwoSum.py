# Two Sum (EASY)
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

class Solution:
  def twoSum(self, nums: list[int], target: int) -> list[int]:
    seen = {}

    for i, n in enumerate(nums):
      diff = target - n
      if diff in seen:
        return [seen[diff], i]
      seen[n] = i

            
sol = Solution()
print(sol.twoSum(nums = [2,7,11,15], target = 9) == [0,1])
print(sol.twoSum(nums = [3,2,4], target = 6) == [1,2])
print(sol.twoSum(nums = [3,3], target = 6) == [0,1])

test = [10,12,13123,41239]
for i in enumerate(test):
  print(i)
