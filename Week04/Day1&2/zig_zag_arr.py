arr=['a','b',1,'c',2,'d',3]
alph=[]
num=[]
for i in range(len(arr)):
  if str(arr[i]).isalpha():
    alph.append(arr[i])
  else:
    num.append(arr[i])
print(alph+num)