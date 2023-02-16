class Solution:
    def rotateRight(self, head, k):
        temp=head
        len=0
        if head==None:
            return None
        while temp:
            temp=temp.next
            len+=1
        temp=head
        temp1=head
        print(len)
        for i in range(len-k%len-1):
            temp1=temp1.next
        nex=temp1.next
        temp1.next=None
        if nex==None:
            return head
        temp2=nex
        while nex and nex.next:
            nex=nex.next
        nex.next=temp
        head=temp2
        return head