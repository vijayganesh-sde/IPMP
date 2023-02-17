# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
      if list1 == None:
          return list2
      if list2 == None:
          return list1
      if list1==None and list2==None:
          return []
      curr1=list1
      curr2=list2
      curr3=dup=ListNode()
      while curr1!=None or curr2!=None:
        curr3.next=ListNode()
        nex3=curr3.next
        if curr1!=None:
            nex1=curr1.next
        if curr2!=None:
            nex2=curr2.next
        if curr1==None:
            print(curr3)
            while curr2!=None:
                curr3.val=curr2.val
                curr2=nex2
                curr3=nex3
            print(dup)
        if curr2==None:
            curr3=curr1
            curr1=None
        if curr1!=None and curr2!=None:
            if curr1.val<curr2.val:
                curr3.val=curr1.val
                curr1=nex1
                curr3=nex3
            else:
                if curr1.val>curr2.val:
                    curr3.val=curr2.val
                    curr2=nex2
                    curr3=nex3
      return dup