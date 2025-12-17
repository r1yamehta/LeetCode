class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:
        NEG = float('-inf')

        dp = [[NEG, NEG, NEG] for _ in range(k + 1)]
        dp[0][0] = 0               
        dp[0][1] = -prices[0]      
        dp[0][2] = prices[0]       

        for price in prices[1:]:
            new_dp = [state[:] for state in dp]

            for t in range(k + 1):
                free, long, short = dp[t]
                new_dp[t][1] = max(new_dp[t][1], free - price)
                new_dp[t][2] = max(new_dp[t][2], free + price)
                if t + 1 <= k:
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], long + price)
                if t + 1 <= k:
                    new_dp[t + 1][0] = max(new_dp[t + 1][0], short - price)

            dp = new_dp

        return max(dp[t][0] for t in range(k + 1))