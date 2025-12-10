class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        mod = 10**9 + 7
        n = len(complexity)

        prefix_min = complexity[0]
        for i in range(1, n):
            if complexity[i] <= prefix_min:
                return 0
            if complexity[i] < prefix_min:
                prefix_min = complexity[i]

        ans = 1
        for k in range(2, n):
            ans = (ans * k) % mod
        return ans
