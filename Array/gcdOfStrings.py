# For two strings s and t, we say "t divides s" 
# if and only if s = t + t + t + ... + t + t 
# (i.e., t is concatenated with itself one or more times). 
# Given two strings str1 and str2, 
# return the largest string x such that x divides both str1 and str2.

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:        
        longer = str1 if len(str1) > len(str2) else str2
        shorter = str1 if longer == str2 else str2
        res = ''
        end = 1
        while (end < len(shorter) + 1):
            candidate1 = longer[:end]
            candidate2 = shorter[:end]
            times1 = int(len(longer) / len(candidate1))
            times2 = int(len(shorter) / len(candidate1))
            if (candidate1 == candidate2) and (candidate1 * times1 == longer) and (candidate2 * times2 == shorter):
                res = candidate1
            end += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    print(sol.gcdOfStrings(str1 = "ABCABC", str2 = "ABC") == "ABC")
    print(sol.gcdOfStrings(str1 = "ABABAB", str2 = "ABAB") == "AB")
    print(sol.gcdOfStrings(str1 = "LEET", str2 = "CODE") == "")
    print(sol.gcdOfStrings(str1 = "AAAAAB", str2 = "AAA") == "")
    print(sol.gcdOfStrings(str1 = "TAUXXTAUXXTAUXXTAUXXTAUXX", str2 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX") == "TAUXX")