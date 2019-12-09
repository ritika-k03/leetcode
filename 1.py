#time_complexity=O(n)

def twoSum(self, a: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(a)):
            if a[i] in d:
                d[a[i]].append(i)
            else:
                d[a[i]]=[i]
        
        for k in d:
            if target-k in d:
                if target-k==k and len(d[k])>1:
                    return [d[k][0],d[k][1]]
                if  target-k!=k:
                    return [d[k][0],d[target-k][0]]
