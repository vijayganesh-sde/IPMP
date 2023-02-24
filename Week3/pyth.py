class Solution:
  def checkTriplet(self,arr, n):
    for i in range(len(arr)):
        arr[i]=arr[i]*arr[i]
    arr.sort()
    l=0
    r=1
    while l!=len(arr)-1:
      if arr[l]+arr[r] in arr[r+1:]:
          return True
    r+=1
    if r==len(arr):
        l+=1
        r=l+1
    return False