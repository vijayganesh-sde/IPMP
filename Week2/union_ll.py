class ListNode:
  def __init__(self,data=0):
    self.val=data
    self.next=None
class Solution:
    def Union(self, headA,headB):
      temp1=headA
      temp2=headB
      listA=[]
      listB=[]
      while temp1:
        listA.append(temp1.val)
      while temp2:
        listB.append(temp2.val)
      listA.sort()
      listB.sort()
      headC=ListNode()
      temp3=headC
      prev=temp3.val
      for i in range(len(listA)):
        if prev==listA[i]:
          continue
        if temp3==None:
          temp3=ListNode(listA[i])
        else:
          temp3.val=listA[i]
        temp3=temp3.next
      for i in range(len(listB)):
        if prev==listB[i]:
          continue
        if temp3==None:
          temp3=ListNode(listB[i])
        else:
          temp3.val=listB[i]
        temp3=temp3.next
      return headC
      