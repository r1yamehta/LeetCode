class Solution:
    def longestBalanced(self, s: str) -> int:
        ans=1
        for i in range(len(s)):
            freq=[0]*26
            distinct=0
            for j in range(i,len(s)):
                index=ord(s[j])-ord('a')
                if freq[index]==0:
                    distinct+=1
                freq[index]+=1

                minf=float('inf')
                maxf=0
                for f in freq:
                    if f>0:
                        minf=min(minf,f)
                        maxf=max(maxf,f)
                
                if minf==maxf:
                    ans=max(ans,j-i+1)

        return ans