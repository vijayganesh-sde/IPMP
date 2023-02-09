def SelectionSort(arr):
    for i in range(len(arr)):
        key=i
        min_ind=i
        for j in range(i+1,len(arr)):
            if arr[min_ind]>arr[j]:
                min_ind=j
        arr[key],arr[min_ind]=arr[min_ind],arr[key]
    print(arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    SelectionSort(arr)