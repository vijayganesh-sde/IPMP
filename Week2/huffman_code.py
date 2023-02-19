import heapq
class node:
  def __init__(self,freq,val,left=None,right=None):
    self.freq=freq
    self.val=val
    self.left=left
    self.right=right
    self.code=''
  def __lt__(self,nxt):
    return self.freq<nxt.freq
def printNodes(node, val=''):
    newVal = val + str(node.code)
    if(node.left):
        printNodes(node.left, newVal)
    if(not node.left and not node.right):
        print(node.val,"->",newVal)
    if(node.right):
        printNodes(node.right, newVal)
    
s="abcabcdabbdccabbdccd"
arr=list(set(s))
freq=[s.count(arr[i]) for i in range(len(arr))]
nodes=[]
for i in range(len(arr)):
  heapq.heappush(nodes,node(freq[i],arr[i]))
print(nodes[0].val)
while len(nodes)>1:
  left=heapq.heappop(nodes)
  right=heapq.heappop(nodes)
  left.code=0
  right.code=1
  new=node(left.freq+right.freq,left.val+right.val,left,right)
  heapq.heappush(nodes,new)
printNodes(nodes[0])