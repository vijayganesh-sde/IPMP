class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
  def hasCycle(self, head) -> bool:
      if head==None:
          return False
      if head.next==None :
          return False
      first=head
      second=head.next
      while first!=second:
          if first==None or first.next==None:
              return False
          first=first.next
          if second==None or second.next==None:
              return False
          second=second.next.next
      return True