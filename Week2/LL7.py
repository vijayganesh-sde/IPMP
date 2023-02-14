class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
    def RemoveCycle(self, head):
      first=head
      second=head
      while second and second.next:
        first=first.next
        second=second.next.next
        if first==second:
          break
      else:
        return None
      temp=head
      while temp!=first:
        temp=temp.next
        first=first.next
      while first.next!=temp:
        first=first.next
      first.next=None
      return head
        
