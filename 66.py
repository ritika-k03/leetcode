#time_complexity= O(n)

def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits] 
        d = int("".join(s))+1
        return [int(i) for i in str(d)]
