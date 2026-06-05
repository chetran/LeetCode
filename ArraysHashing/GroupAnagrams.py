# Group Anagrams (MEDIUM)

# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

class Solution:
  def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
    anagrams = {}
    
    for word in strs: 
      char_freq = [0] * 26
      for c in word:
        index = ord(c) - ord('a')
        char_freq[index] += 1
      char_freq = str(char_freq)
      if char_freq in anagrams:
        anagrams[char_freq].append(word)
      else:
        anagrams[char_freq] = [word]

    return [list for char_freq, list in anagrams.items()]


sol = Solution()
print(sol.groupAnagrams(strs = ["act","pots","tops","cat","stop","hat"]) == [["hat"],["act", "cat"],["stop", "pots", "tops"]])
#print(sol.groupAnagrams(strs = ["x"]) == [["x"]])
#print(sol.groupAnagrams(strs = [""]) == [[""]])
