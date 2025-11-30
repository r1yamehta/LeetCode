class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total=sum(nums)
        rem = total % p
        if rem == 0:
            return 0  

        seen={0: 0} 
        ans=len(nums)
        cur=0

        for i,val in enumerate(nums, start=1):
            cur=(cur+val) % p
            target=(cur-rem) % p 

            if target in seen:
                ans=min(ans,i-seen[target])
            seen[cur]=i

        return ans if ans<len(nums) else -1
