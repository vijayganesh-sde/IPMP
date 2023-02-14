class ListNode:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
    def reverseList(self, head):
      prev=None
      curr=head
      while curr!=None:
        nex=curr.next
        curr.next=prev
        prev=curr
        curr=nex
      head=prev
      return (head)
