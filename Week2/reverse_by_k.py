# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head, k: int):
        temp=head
        l=0
        arr=[]
        while temp:
            temp=temp.next
            l+=1
        temp=head
        temp1=head
        for i in range(l//k):
            for j in range(k-1):
                temp1=temp1.next
            nex=temp1.next
            temp1.next=None
            arr.append(self.reverse(temp))
            temp1=nex
            temp=nex
        arr.append(temp)
        for i in range(len(arr)-1):
            temp=arr[i]
            temp1=arr[i]
            nex=arr[i+1]
            while temp1.next:
                temp1=temp1.next
            temp1.next=nex
            arr[i+1]=temp
        return arr[-1]
            
    def reverse(self,head):
        prev=None
        curr=head
        while curr!=None:
            nex=curr.next
            curr.next=prev
            prev=curr
            curr=nex
        head=prev
        return head
