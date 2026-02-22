class Solution:
    def binaryGap(self, n: int) -> int:
        prev=0
        distance=0
        s=bin(n)[2:]
        for i in range(len(s)):
            if s[i]=='1':
                distance=max(distance,i-prev)
                prev=i

        return distance
            

