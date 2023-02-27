import math
class Solution:
	def findRank(self, S):
    l=list(S)
    l.sort()
    rank=0
    for i in range(len(S)):
      ind=l.index(S[i])
      rank=rank+int(ind*math.factorial(len(S)-i-1))
      l.pop(ind)
    return rank+1