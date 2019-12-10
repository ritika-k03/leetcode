#time_complexity=O(n^2)
#space_complexity=O(1)

def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p=m
        q=0
        for i in range(n):
            nums1[p]=nums2[i]
            p+=1
        for i in range(m+n-1):
            for j in range(m+n-1):
                if(nums1[j]>nums1[j+1]):
                    nums1[j],nums1[j+1]=nums1[j+1],nums1[j]
        
