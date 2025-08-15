class Solution:
  def encode(self, strs: list[str]) -> str:
      res = ""
      for s in strs:
          res += (str(len(s))+"#"+s)

      return res
  
  def decode(self, s: str) -> list[str]:
    res, i = [], 0

    while i < len(s):
      j = i
      while True:
        if s[j] == "#":
          wordLength = int(s[i:j])
          res.append(s[j + 1:j + wordLength + 1])
          i = j + wordLength + 1
          break
        j += 1
    return (res)

        
      

            
            

                

sol = Solution()
test = ["","   ","!@#$%^&*()_+","LongStringWithNoSpaces","Another, String With, Commas"]
#test = ["","   "]
a = sol.encode(test)
print(a)
b = sol.decode(a)
print(b)
print(test)
print(b == test)
for i in range(len(b)):
  if b[i] != test[i]:
    print(b[i], "VS", test[i])
