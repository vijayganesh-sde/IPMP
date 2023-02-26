class node:
  def __init__(self,val):
    self.val=val
    self.next=None
class Solution:
    def skipMdeleteN(self, head, M, N):
      # Code here
      temp=head
      temp1=head
      c=0
      while c!=M-1:
          c+=1
          temp=temp.next
      c=0
      while c!=(M+N):
          c+=1
          temp1=temp1.next
      temp.next=temp1
      return head
s=Solution()
head=node(9)
head.next=node(1)
head.next.next=node(3)
head.next.next.next=node(5)
head.next.next.next.next=node(9)
head.next.next.next.next.next=node(4)
h=s.skipMdeleteN(head,2,1)
while h!=None:
  print(h.val,end=" ")
  h=h.next