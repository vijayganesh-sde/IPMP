matrix=[[1,2,3,1],[0,3,1,1,1],[0,3,1,1,2]]
max_till=-1
row=-1
for i in range(len(matrix)): 
  if matrix[i].count(1)>max_till:
    max_till=matrix[i].count(1)
    row=i
print("row is",row,"and count is",max_till)
