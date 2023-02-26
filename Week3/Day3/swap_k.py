class Solution:
    def swapNodes(self, head, k: int):
        temp=head
        temp1=head
        len=0
        while temp!=None:
            len+=1
            temp=temp.next
        temp=head
        c=0
        while c!=k-1:
            c+=1
            temp=temp.next
        c=0
        while c!=len-k:
            c+=1
            temp1=temp1.next
        temp.val,temp1.val=temp1.val,temp.val
        return head