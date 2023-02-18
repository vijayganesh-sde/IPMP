class node:
    def __init__(self, val):
        self.data = val
        self.next = None
class Solution:
    def arrangeCV(self, head):
        # Code here
        temp=head
        vow=None
        cons=None
        while temp:
            if temp.data in ['a','e','u','i','o']:
                if vow==None:
                    vow=node(temp.data)
                    v_temp=vow
                else:
                    v_temp.next=node(temp.data)
                    v_temp=v_temp.next
            else:
                if cons==None:
                    cons=node(temp.data)
                    c_temp=cons
                else:
                    c_temp.next=node(temp.data)
                    c_temp=c_temp.next
            temp=temp.next
        head=cons
        while cons and cons.next:
            cons=cons.next
        if cons:
            cons.next=vow
        else:
            head=vow
        return head