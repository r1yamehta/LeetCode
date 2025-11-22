class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        opr=0
        for i in range(len(nums)):
            if nums[i]%3==0:
                pass
            else:
                opr+=1
        return opr
