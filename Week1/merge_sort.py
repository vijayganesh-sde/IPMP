def merge(arr,i,m,j):
  begin=i
  final=m+1
  k=i
  L=arr[i:m]
  R=arr[m+1:j]
  while begin<=m and final<j:
    if arr[begin]>arr[final]:
      arr[k]=R[final]
      final+=1
    else:
      arr[k]=L[begin]
      begin+=1
    k+=1
  while final<j:
    arr[k]=R[final]
    final+=1
    k+=1
  while begin<m:
    arr[k]=L[begin]
    begin+=1
    k+=1
def mergeSort(arr,start,end):
  if start<end:
    mid=int((end+start)/2)
    mergeSort(arr,start,mid)
    mergeSort(arr,mid+1,end)
    merge(arr,start,mid,end)
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
mergeSort(arr,0,n-1)
print(arr)