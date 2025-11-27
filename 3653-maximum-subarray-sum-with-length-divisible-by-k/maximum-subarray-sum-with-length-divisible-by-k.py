class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        inf = float('inf')
        pref = 0
        lowest = [float('inf')] * k
        lowest[0] = 0
        
        ans = -inf
        
        for i, x in enumerate(nums):
            pref += x
            mod = (i + 1) % k 
            ans = max(ans, pref - lowest[mod])
            lowest[mod] = min(lowest[mod], pref)

        return ans
