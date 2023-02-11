arr=[1,2,3,3,3,4,4,5,6]
l=0
r=len(arr)-1
count=0
def Count(arr,start,end,target):
  global count
  if start<=end:
    mid=(start+end)//2
    if target==arr[mid]:
      count+=1
    Count(arr,start,mid-1,target)
    Count(arr,mid+1,end,target)
Count(arr,0,len(arr)-1,4)
print(count)
