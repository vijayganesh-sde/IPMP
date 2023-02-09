def Bsort(a):
  swap=0
  for i in range(len(a)):
      for j in range(1,len(a)-i):
          if a[j-1]>a[j]:
              a[j-1],a[j]=a[j],a[j-1]
              swap+=1
  print("Array is sorted in",swap,"swaps.")
  print("Sorted array is",a)
if __name__ == '__main__':
  n = int(input().strip())
  a = list(map(int, input().rstrip().split()))
  Bsort(a)
