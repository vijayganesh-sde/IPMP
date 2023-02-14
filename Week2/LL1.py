class ListNode:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
    def removeNthFromEnd(self, head, n) :
        curr=dup=head
        len_list=length(curr)
        loc=len_list-n+1
        c=0
        while curr!=None:
            nex=curr.next
            c+=1
            if c==loc:
                if c==1:
                    return curr.next
                dup.next=curr.next
                return head
            if c<loc-1:
                dup=dup.next
            curr=nex
def length(ll):
    k=0
    while ll.next!=None:
        nex=ll.next
        ll=nex
        k+=1
    return k+1
