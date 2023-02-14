class Node:
  def __init__(self,data):
    self.val=data
    self.next=None
class Solution:
  def deleteNode(self, node):
    temp=node
    temp=temp.next
    node.val=temp.val
    node.next=node.next.next