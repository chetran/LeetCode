class Solution:
  def threeSum(self, nums : list[int]) -> list[list[int]]:
    n = len(nums)
    res = set()
    for i in range(n):
      for j in range(n - 1, -1, -1):
        target = -nums[i] - nums[j]
        res.add(frozenset([nums[i], nums[j], target]))
    print([list(x) for x in res])
        
        


sol = Solution()
#print(sol.threeSum([-1,0,1,2,-1,-4]))
print(sol.threeSum([0,1,1]))
