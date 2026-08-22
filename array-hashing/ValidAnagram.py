# Valid Anagram (EASY)
# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      char = {}
      
      for i in s: 
        char[i] = 1 + char.get(i, 0)

      for i in t:
        if i not in char or char[i] == 0:
          return False
        char[i] -= 1

      return True if len(s) == len(t) else False
            


sol = Solution()
print(sol.isAnagram(s = "racecar", t = "carrace") == True)
print(sol.isAnagram(s = "jar", t = "jam") == False)
