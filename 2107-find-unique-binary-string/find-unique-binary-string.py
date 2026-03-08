class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans=""
        for i in range(len(nums)):
            a= 1-int(nums[i][i])
            ans+=str(a)
        return ans