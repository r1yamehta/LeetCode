class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        l,r=0,sum(batteries)//n

        def check(time):
            use=0
            for i in batteries:
                use+=min(i,time)
            return use>=n*time
        
        answer=0
        while l<=r:
            mid=(l+r)//2
            if check(mid):
                answer=mid
                l=mid+1
            else:
                r=mid-1
        return answer
