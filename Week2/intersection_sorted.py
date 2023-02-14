class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
    def getIntersectionNodeOfSorted(self, headA, headB):
        temp=headA
        temp1=headB
        while temp and temp1:
          if temp.val==temp1.val:
            if temp==temp1:
              return temp
            else:
              temp,temp1=temp.next,temp1.next
          if temp.val<temp1.val:
            temp=temp.next
          if temp.val>temp1.val:
            temp1=temp1.next
        return -1
            
              