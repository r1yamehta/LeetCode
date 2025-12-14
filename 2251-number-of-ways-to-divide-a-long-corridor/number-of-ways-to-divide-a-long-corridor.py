class Solution:
    def numberOfWays(self, corridor: str) -> int:
        mod=10**9+7
        ways = 1
        seat_count = 0
        plant_gap = 0
        total=corridor.count("S")
        if total==0 or total%2!=0:
            return 0
        for ch in corridor:
            if ch=='S':
                seat_count+=1
                if seat_count>2 and seat_count%2==1:
                    ways*=(plant_gap+1)
                    plant_gap=0
            else:
                if seat_count%2==0 and seat_count>=2:
                    plant_gap+=1 
        return ways%mod