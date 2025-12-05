class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        # total=sum(nums)
        
        # if total%2!=0:
        #     return 0
        # return len(nums)-1

        total=sum(nums)
        left=0
        count=0
        for i in range(len(nums)-1):
            left+=nums[i]
            right=total-left
            if (right-left)%2==0:
                count+=1
        return count
        

