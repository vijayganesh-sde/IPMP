class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
    def getIntersectionNode(self, headA, headB):
        temp=headA
        temp1=headB
        c1=0
        c2=0
        while(temp!=None):
            c1+=1
            temp=temp.next
        while(temp1!=None):
            c2+=1
            temp1=temp1.next
        temp=headA
        temp1=headB
        if(c1<c2):
            d=c2-c1
            for i in range(d):
                temp1=temp1.next
            while(temp!=None):
                if(temp==temp1):
                    return temp
                temp1=temp1.next
                temp=temp.next
        else:
            d=c1-c2
            for i in range(d):
                temp=temp.next
            while(temp1!=None):
                if(temp==temp1):
                    return temp
                temp=temp.next
                temp1=temp1.next
