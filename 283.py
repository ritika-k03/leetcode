#time_complexity=O(n^2)

def moveZeroes(self, nums: List[int]) -> None:
        if 0 in nums:
            for i in range(len(nums)):
                p=nums.index(0)
                for j in range(p+1,len(nums)):
                    if nums[j]!=0:
                        nums[p],nums[j]=nums[j],nums[p]
                        p=j
