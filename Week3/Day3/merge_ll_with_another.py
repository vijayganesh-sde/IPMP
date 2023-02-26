class Solution:
    def mergeInBetween(self, list1, a: int, b: int, list2):
        c=0
        temp=list1
        temp1=list1
        while c!=a-1:
            c+=1
            temp=temp.next
        c=0
        while c!=b+1:
            c+=1
            temp1=temp1.next
        temp.next=list2
        while temp.next:
            temp=temp.next
        temp.next=temp1
        return list1