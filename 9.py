#time_complexity=O(1)
#space_complexity=O(1)

def isPalindrome(self, x: int) -> bool:
        if str(x)!=str(x)[::-1]:
            return False
        else:
            return True
