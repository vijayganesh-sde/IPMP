import heapq
class ListNode:
  def __init__(self,val):
    self.val=val
    self.next=None
class Solution:
    def mergeKLists(self, lists):
        arr=[]
        for i in range(len(lists)):
            temp=lists[i]
            while temp:
                heapq.heappush(arr,temp.val)
                temp=temp.next
        head=None
        for i in range(len(arr)):
            val=heapq.heappop(arr)
            if head==None:
                head=ListNode(val)
                temp=head
            else:
                temp.next=ListNode(val)
                temp=temp.next
        return head
        
        
