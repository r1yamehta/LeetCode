class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans=0
        mod=10**9 + 7
        for i in range(1,n+1):
            blen=i.bit_length()
            ans=(ans<<blen | i) % mod
        return ans 