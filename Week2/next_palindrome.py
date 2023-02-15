def isPalindrome(num):
  if str(num)==str(num)[::-1]:
    return 1
  return 0
num=1243234
while not(isPalindrome(num)):
  num+=1
print(num)
'''alternative algorithm--'''
def generateNextPalindrome(self,num, n ):
  l=0
  r=n-1
  flag=0
  while(l!=r and l!=r-1):
      if r-l==2 or r-l==3:
          if num[l]>num[r]:
              flag=1
      if num[l]!=num[r]:
          num[r]=num[l]
      l+=1
      r-=1
  if l==r-1:
      if flag:
          if num[l]>num[r]:
              num[l]=num[r]+1
              num[r]=num[l]
          else:
              num[r]=num[l]+1
              num[l]=num[r]
      else:
          if num[l]>num[r]:
              num[r]=num[l]
          else:
              num[l]=num[r]
  if l==r:
      if num[l]==9:
          while l>=0 and num[l]==9:
              num[l]=0
              l-=1
          if l>0:
              num[l]+=1
          if l==-1:
              num.insert(0,1)
          l=0
          r=len(num)-1
          while(l!=r and l!=r-1):
              if num[l]!=num[r]:
                  num[r]=num[l]
              l+=1
              r-=1
      else:
          if not(flag):
              num[l]+=1
  return num
                
