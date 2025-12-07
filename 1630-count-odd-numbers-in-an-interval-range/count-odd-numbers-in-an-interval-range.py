class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if low%2==0:
            low+=1
        return len(range(low,high+1,2))