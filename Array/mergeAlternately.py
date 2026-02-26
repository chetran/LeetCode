import math

# You are given two strings word1 and word2. 
# Merge the strings by adding letters in alternating order, starting with word1. 
# If a string is longer than the other, append the additional letters onto the end of the merged string.

# The first solution in mind is just to create an empty string, loop through both words, 
# and successively add a letter. If a word is out of letters, the remaining of the other word,
# is added and returned. 

# TIme Complexity, since at most, it will iterate through both strings so O(m + n)

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = ''
        total_len = len(word1) + len(word2)
        for i in range(total_len):
            idx = math.floor(i / 2)
            if (i % 2 == 0) and idx >= len(word1):
                return res + word2[idx:]
            elif (i % 2 == 0):
                res += word1[idx]
            elif (i % 2 != 0) and idx >= len(word2):
                return res + word1[idx + 1:]
            else:
                res += word2[idx]
        
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.mergeAlternately(word1 = "abc", word2 = "pqr") == "apbqcr")
    print(sol.mergeAlternately(word1 = "ab", word2 = "pqrs") == "apbqrs")
    print(sol.mergeAlternately(word1 = "abcd", word2 = "pq") == "apbqcd")