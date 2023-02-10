arr=[1,2,3,3,3,4,4,5,6]
l=0
r=len(arr)-1
key=arr[(l+r)//2]
count=0
def findMax(arr,start,end):
  global count
  if start<=end:
    mid=(start+end)//2
    if key==arr[mid]:
      count+=1
    findMax(arr,start,mid-1)
    findMax(arr,mid+1,end)
findMax(arr,0,len(arr)-1)
if count>len(arr)/2:
  print(1)
else:
  print(0)
  
