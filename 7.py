#time_complexity= O(n)
#space_complexity=O(1)

def reverse(self, x: int) -> int:
        if(x<0):
            s=str(x)[1:]
        else:
            s=str(x)
        s=s[::-1]
        zero_count=0
        for i in s:
            if(i!=0):
                break
            zero_count+=1
        if(x<0):
            final= int("-"+s[zero_count:])
        else:
            final= int(s[zero_count:])
        if -2**31<=final<=2**31-1:
            return final
        else:
            return 0
