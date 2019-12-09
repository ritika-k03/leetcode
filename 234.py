#time_complexity=O(n)

def isPalindrome(self, head: ListNode) -> bool:
        s=[]
        while head!=None:
            s.append(head.val)
            head=head.next
        if(s==s[::-1]):
            return True
        return False
