class ListNode:
  def __init__(self,data=0):
    self.val=data
    self.next=None
class Solution:
    def DeleteAlternativeNodes(self, head):
      first=head
      second=head
      while second.next:
        second=second.next.next
        first.next=second
        first=first.next
      return head
      
      