class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ans=[0]*len(nums)
        for i,n in enumerate(nums):
            l=0
            for j in range(len(nums)):
                if n > nums[j] :
                    l+=1
            ans[i]=l
        return ans
