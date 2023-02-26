class ListNode:
  def __init__(self,val):
    self.val=val
    self.next=None
class Solution:
  def multiply(self, l1, l2):
    n1=""
    n2=""
    while l1!=None:
      n1+=str(l1.val)
      l1=l1.next
    while l2!=None:
      n2+=str(l2.val)
      l2=l2.next
    return int(n1)*int(n2)
head1=ListNode(6)
head1.next=ListNode(9)
head1.next.next=ListNode(0)
head2=ListNode(2)
head2.next=ListNode(5)
s=Solution()
print(s.multiply(head1,head2))
