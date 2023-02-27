def permute(s, answer):
  if (len(s) == 0):
    return
  for i in range(len(s)):
    ch = s[i]
    left_substr = s[0:i]
    right_substr = s[i + 1:]
    rest = left_substr + right_substr
    print(rest,answer)
    permute(rest, answer+ch)
answer = ""
s = "ABC"
print("All possible strings are : ")
permute(s, answer)