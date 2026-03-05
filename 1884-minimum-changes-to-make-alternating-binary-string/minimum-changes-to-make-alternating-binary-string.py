class Solution:
    def minOperations(self, s: str) -> int:
        ans=sum(index%2==int(val) for index,val in enumerate(s))
        return min(ans,len(s)-ans)
            
            