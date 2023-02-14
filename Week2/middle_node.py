class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
    def middleNode(self, head):
        temp=head
        if head==None: return None
        else:
            first=head
            second=head
            while(second.next!=None):
                if(second.next.next==None):
                
                    first=first.next
                    second=second.next
                else:
                    first=first.next
                    second=second.next.next
        return first