import heapq

class Solution:
  def longestConsecutive(self, nums : list[int]) -> int:
    longest = 0 

    for num in nums:
      if not (num - 1) in nums:
        counter = 1
        while (num + counter) in nums:
          counter += 1 
        if longest < counter:
          longest = counter
    return longest

          
sol = Solution()
print(sol.longestConsecutive([2,20,4,10,3,4,5]))
print(sol.longestConsecutive([0,3,2,5,4,6,1,1]))
print(sol.longestConsecutive([]))
