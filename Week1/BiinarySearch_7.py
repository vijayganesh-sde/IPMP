arr=[-10,-3,-1,1,5,6,7,10]
def fixedPoint(arr):
  l=0
  r=len(arr)-1
  while l<=r:
    mid=(l+r)//2
    if arr[mid]==mid:
      return mid
    if arr[mid]<mid:
      l=mid+1
    if arr[mid]>mid:
      r=mid-1
  return -1
print(fixedPoint(arr))
