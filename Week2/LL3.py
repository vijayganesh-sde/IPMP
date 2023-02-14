class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
def recurse(head):
  if head==None:
    return
  recurse(head.next)
  print(head.val,end=" ")
head=Node(5)
head.next=Node(10)
head.next.next=Node(20)
recurse(head)
