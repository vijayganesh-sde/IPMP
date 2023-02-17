class ListNode:
  def __init__(self, val, next=None):
    self.val = val
    self.next = next
class Solution:
    def Sorted012(self, head):
      temp=head
      zer_count=0
      one_count=0
      two_count=0
      while temp:
        if temp.val==0:
          zer_count+=1
        if temp.val==1:
          one_count+=1
        if temp.val==2:
          two_count+=1
        temp=temp.next
      head1=None
      while zer_count:
        if head1==None:
          head1=ListNode(0)
          temp=head1
        
        else:
          temp.next=ListNode(0)
          temp=temp.next
        zer_count-=1
      while one_count:
        if head1==None:
          head1=ListNode(1)
          temp=head1
        else:
          temp.next=ListNode(1)
          temp=temp.next
        one_count-=1
      while two_count:
        if head1==None:
          head1=ListNode(2)
          temp=head1
        else:
          temp.next=ListNode(2)
          temp=temp.next
        two_count-=1
      return head1
head=ListNode(1)
head.next=ListNode(2)
head.next.next=ListNode(0)
head.next.next.next=ListNode(1)
s=Solution()
h=s.Sorted012(head)
while h:
  print(h.val)
  h=h.next