class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row=0
        col=0
        start_row=0
        start_col=0
        end_row=len(matrix)-1
        end_col=len(matrix[0])-1
        c=0
        arr=[]
        while c<=len(matrix)*len(matrix[0]):
            if c==len(matrix)*len(matrix[0]):
                break
            while col<=end_col:
                c+=1
                arr.append(matrix[row][col])
                col+=1
            start_row+=1
            col-=1
            row=start_row
            if c==len(matrix)*len(matrix[0]):
                break
            while row<=end_row:
                c+=1
                arr.append(matrix[row][col])
                row+=1
            end_col-=1
            row-=1
            col=end_col
            if c==len(matrix)*len(matrix[0]):
                break
            while col>=start_col:
                c+=1
                arr.append(matrix[row][col])
                col-=1
            end_row-=1
            col+=1
            row=end_row
            if c==len(matrix)*len(matrix[0]):
                break
            while row>=start_row:
                c+=1
                arr.append(matrix[row][col])
                row-=1
            start_col+=1
            row+=1
            col=start_col
            print(arr)
        return arr
            
