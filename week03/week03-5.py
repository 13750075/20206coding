#week03-5.py
#1493.
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        N=len(nums)
        tail=0
        zeros=0
        ans=0
        for head in range(N):
            if  nums[head]==0:zeros+=1
            while zeros>1:
                if nums[tail]==0:zeros-=1
                tail+=1
            ans=max(ans,head-tail+1)
        return ans-1
