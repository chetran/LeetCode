# Contains duplicate problem (EASY)
# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:
      seen = set()
      for i in nums:
        if i in seen:
          return True
        else:
          seen.add(i)
    
sol = Solution()
print(sol.hasDuplicate([1, 2, 3, 3]))
