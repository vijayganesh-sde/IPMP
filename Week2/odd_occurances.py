def oddOccurances(arr):
  d={}
  for i in range(len(arr)):
    if arr[i] not in d:
      d[arr[i]]=1
    else:
      d[arr[i]]+=1
  for key in d:
    if d[key]%2:
      return key
  return -1
  