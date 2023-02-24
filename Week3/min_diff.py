class Solution:
    def minimumAbsDifference(self, arr):
        arr.sort()
        min_diff=10000
        temp=[]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]<min_diff:
                min_diff=arr[i+1]-arr[i]
        for i in range(len(arr)-1):
            if arr[i+1]-arr[i]==min_diff:
                temp.append([arr[i],arr[i+1]])
        return temp