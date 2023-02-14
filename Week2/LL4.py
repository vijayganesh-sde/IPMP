class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
  def isPalindrome(self, head) -> bool:
    temp=head
    prev=None
    curr=temp
    nex=temp.next
    str1=""
    str2=""
    while(temp!=None):
        str1+=str(temp.val)
        temp=temp.next
    
    while(nex!=None):
        curr.next=prev
        prev=curr
        curr=nex
        nex=nex.next
    curr.next=prev
    while curr!=None:
        str2+=str(curr.val)
        curr=curr.next
    if(str1==str2) : 
        return True 
    return False
