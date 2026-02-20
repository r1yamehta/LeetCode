class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        if not s:
            return ""

        balance=0
        left=0
        special_blocks=[]
        for i,j in enumerate(s):
            if j=='1':
                balance+=1
            else: 
                balance-=1
            if balance==0:
                instr=s[left+1:i]
                optimized_inner = self.makeLargestSpecial(instr)
                special_blocks.append("1" + optimized_inner + "0")
                left=i+1

        special_blocks.sort(reverse=True)

        return "".join(special_blocks)