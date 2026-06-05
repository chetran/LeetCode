class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
      #print(f'NUMS: {nums}')
      prefix = [1]
      suffix = [1]
      for i in range(0, len(nums) - 1, 1):
          prefix.append(prefix[i]*nums[i])
      #print(prefix)
      for i in range(len(nums) - 1, 0, -1):
          suffix.append(suffix[len(nums) - 1 - i]*nums[i])

      #print(suffix)

      return [prefix[i]*suffix[len(nums)-i-1] for i in range(len(nums))]

    def optimal(self, nums: list[int]) -> list[int]:
      n = len(nums)
      res = [1] * n
      prefix = 1
      for i in range(n):
        res[i] = prefix
        prefix *= nums[i]
      
      postfix = 1  
      for i in range(n - 1, -1, -1):
        res[i] *= postfix
        postfix *= nums[i]
        
      return res

sol = Solution()
print(sol.optimal([1,2,4,6]) == [48,24,12,8])
print(sol.optimal([-1,0,1,2,3]) )
print(sol.optimal([1,2,3,4]) )
