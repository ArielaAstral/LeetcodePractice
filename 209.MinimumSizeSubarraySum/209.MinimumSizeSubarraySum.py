class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        s=0
        start=0
        minm=float('inf')
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                minm=min(i-start+1,minm)
                s-=nums[start]
                start+=1
        if minm==float('inf'):
            return 0
        else:
            return minm        
