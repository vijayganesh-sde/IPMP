class Solution:
  def reverseString(self, s) :
    l=len(s)
    if l==1:
        return s
    s=self.reverseString(s[l//2:])+self.reverseString(s[:l//2])
    return s
sol=Solution()
print(sol.reverseString(['a','s','e','d']))
