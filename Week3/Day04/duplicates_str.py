class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack=[]
        d={}
        s_set=set()
        for i in range(len(s)):
            d[s[i]]=i
        for i in range(len(s)):
            if s[i] not in s_set:
                while stack and stack[-1]>s[i] and d[stack[-1]]>i:
                    s_set.remove(stack.pop())
                s_set.add(s[i])
                stack.append(s[i])
        return ''.join(stack)
                