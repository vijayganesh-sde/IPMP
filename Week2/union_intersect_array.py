def union(arr1,arr2):
  l1=0
  l2=0
  arr=[]
  while l1!=len(arr1) and l2!=len(arr2):
    if arr1[l1]==arr2[l2]:
      arr.append(arr1[l1])
      l1+=1
      l2+=1
    elif arr1[l1]>arr2[l2]:
      arr.append(arr2[l2])
      l2+=1
    elif arr1[l1]<arr2[l2]:
      arr.append(arr1[l1])
      l1+=1
  while l1!=len(arr1):
    arr.append(arr1[l1])
    l1+=1
  while l2!=len(arr2):
    arr.append(arr2[l2])
    l2+=1
  return arr
def intersection(arr1, arr2):
  l1=0
  l2=0
  arr=[]
  while l1!=len(arr1) and l2!=len(arr2):
    if arr1[l1]==arr2[l2]:
      arr.append(arr1[l1])
      l1+=1
      l2+=1
    elif arr1[l1]>arr2[l2]:
      l2+=1
    elif arr1[l1]<arr2[l2]:
      l1+=1
  return arr
arr1=[2,3,5,7,8,9]
arr2=[3,5,7,9,10,23,45]
print(union(arr1,arr2))
print(intersection(arr1,arr2))