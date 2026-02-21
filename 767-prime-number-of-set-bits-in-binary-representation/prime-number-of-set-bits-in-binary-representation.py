class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def checkprime(n):
            for i in range(2,int(n**.5)+1):
                if n%i==0:
                    return False
            return True if n>1 else False

        result=0
        for i in range(left,right+1):
            if checkprime(i.bit_count()):
                result+=1

        return result

