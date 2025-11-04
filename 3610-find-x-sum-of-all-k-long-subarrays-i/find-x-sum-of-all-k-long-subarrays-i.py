class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
    
        n = len(nums)
        result = []
        
        for i in range(n - k + 1):
            sub = nums[i:i+k]
            freq = collections.Counter(sub)
            
            sorted_items = sorted(freq.items(), key=lambda a: (-a[1], -a[0]))
            
            top_x = {val for val, count in sorted_items[:x]}
            
            total = sum(num for num in sub if num in top_x)
            result.append(total)
        
        return result
