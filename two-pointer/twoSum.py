class Solution:
  def twoSum(self, numbers : list[int], target : int ) -> list[int]: 
    n = len(numbers)
    for i in range(n - 1, -1, -1):
      diff = target - numbers[i]
      if diff in numbers and numbers.index(diff) != i:
        return [numbers.index(diff) + 1, i + 1]

sol = Solution()
print(sol.twoSum([1,2,3,4], 3))
#print(sol.twoSum([1,2,3,4], 3))
