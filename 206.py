#time_complexity=O(n)

def reverseList(self, head: ListNode) -> ListNode:
        s=[]
        h=head
        while h!=None:
            s.append(h.val)
            h=h.next
        
        x=head
        while head!=None:
            head.val=s[-1]
            s.pop()
            head=head.next
        return x
