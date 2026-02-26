class Solution:
    def numSteps(self, s: str) -> int:
        count=0

        while s!='1':
            if s[-1]=='0':
                s=s[:-1]
            else:
                s=bin(int(s,2)+1)[2:]
            count+=1

        return count
            
            

