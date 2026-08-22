class Solution:
  def isPalindrome(self, s : str) -> bool:
    print("LENGTH:", len(s))
    j = len(s) - 1
    i = 0
    while i <= j:
      print(i, j)
      if s[i].lower() != s[j].lower():
        if not s[j].isalnum():
          j -= 1
          continue
        if not s[i].isalnum():
          i += 1 
          continue
        print(i, s[i].lower())
        print(j,  s[j].lower())
        return False
      i += 1 
      j -= 1
    return True

sol = Solution()
print(sol.isPalindrome("Was it a car or a cat i saw?") == True)
print(sol.isPalindrome("tab a cat") == False)
print(sol.isPalindrome("ab") == False)
