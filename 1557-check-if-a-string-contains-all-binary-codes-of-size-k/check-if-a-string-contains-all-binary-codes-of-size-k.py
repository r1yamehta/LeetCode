class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        all=set()
        for i in range(len(s)-k+1):
            a=s[i:i+k]
            if a not in all:
                all.add(a)

        return True if len(all)==2**k else False

