class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n=len(grid)

        def count_trail(arr):
            ans=0
            for i in range(n-1,-1,-1):
                if arr[i]==0:
                    ans+=1 
                else:
                    break
            return ans

        arr=[count_trail(row) for row in grid]
        steps=0
        for i in range(n):
            target=n-i-1
            if arr[i]<target:
                flag=False
                for j in range(i+1,n):
                    if arr[j]>=target:
                        steps+=j-i
                        arr[i+1:j+1]=arr[i:j]
                        flag=True
                        break
                if not flag:
                    return -1
        return steps
                        
                    
                



        