class Solution:
    def flatten(self, head):
        arr=[head]
        arr_count=0
        left=[]
        if not head:
            return head
        while arr_count<len(arr):
            temp=arr[arr_count]
            while temp and temp.child==None:
                temp=temp.next
            if temp and temp.child:
                if temp.next:
                    left.append(temp.next)
                temp.next=None
                arr.append(temp.child)
                temp.child=None
            else:
                break
            arr_count+=1
        for i in range(len(arr)-1):
            temp=arr[i]
            while temp.next:
                temp=temp.next
            temp.next=arr[i+1]
            arr[i+1].prev=temp
            arr[i+1]=arr[i]
        if left:
            temp=arr[-1]
            while temp.next:
                temp=temp.next
            temp.next=left[-1]
            left[-1].prev=temp
            left[-1]=arr[-1]
            for i in range(len(left)-1,0,-1):
                temp=left[i]
                while temp.next:
                    temp=temp.next
                temp.next=left[i-1]
                left[i-1].prev=temp
                left[i-1]=left[i]
            head=left[0]
            return head
        else:
            return arr[-1]