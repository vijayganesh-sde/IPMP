class ListNode:
  def __init__(self,val):
    self.val=val
    self.next=None
class Solution:
  def addTwoNumbers(self, l1, l2):
      arr=[]
      arr1=[]
      while l1!=None or l2!=None:
        if l1!=None:
            arr.append(str(l1.val))
            l1=l1.next
        if l2!=None:
            arr1.append(str(l2.val))
            l2=l2.next
      print(arr1, arr)
      arr.reverse()
      arr1.reverse()
      arr=[int(x) for x in str(int("".join(arr))+int("".join(arr1)))]
      arr.reverse()
      print(arr)
      for i in range(len(arr)):
          arr[i]=ListNode(val=arr[i])
      for i in range(len(arr)-1):
          arr[i].next=arr[i+1]
      return (arr[0])
