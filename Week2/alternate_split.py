# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def Split(self, head):
      if head==None:
          return head
      even_temp=head
      odd_temp=head.next
      e=even_temp
      o=odd_temp
      while e and o and e.next and o.next:
          print(e.val,o.val)
          e.next=e.next.next
          o.next=o.next.next
          e=e.next
          o=o.next
      if e and e.next:
          e.next=e.next.next
      if o and o.next:
          o.next=o.next.next
      return [even_temp,odd_temp]