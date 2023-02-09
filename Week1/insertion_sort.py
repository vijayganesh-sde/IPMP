def insertionSort(n, arr):
    # Write your code here
    for unsorted_ptr in range(1,n):
        sorted_ptr=unsorted_ptr-1
        key=arr[unsorted_ptr]
        while sorted_ptr>=0:
            if arr[sorted_ptr]>key:
                arr[sorted_ptr],arr[unsorted_ptr]=arr[unsorted_ptr],arr[sorted_ptr]
                sorted_ptr-=1
                unsorted_ptr-=1
            else:
                break
    print("sorted array is ",arr)
if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))
    insertionSort(n, arr)