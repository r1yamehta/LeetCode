class Solution:
    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
       
        adj = [[] for _ in range(n)]
        for u, v in hierarchy:
            adj[u-1].append(v-1) 
        def merge(dp_target, dp_source):
            new_dp = [-float('inf')] * (budget + 1)
            for b_curr in range(budget + 1):
                if dp_target[b_curr] == -float('inf'): 
                    continue
                
                for b_child in range(budget + 1 - b_curr):
                    if dp_source[b_child] == -float('inf'): 
                        continue
                    
                    if dp_target[b_curr] + dp_source[b_child] > new_dp[b_curr + b_child]:
                        new_dp[b_curr + b_child] = dp_target[b_curr] + dp_source[b_child]
            return new_dp

        def dfs(u):
            kids_if_u_does_not_buy = [-float('inf')] * (budget + 1)
            kids_if_u_does_not_buy[0] = 0
            
            kids_if_u_buys = [-float('inf')] * (budget + 1)
            kids_if_u_buys[0] = 0

            for v in adj[u]:
                child_res_0, child_res_1 = dfs(v)

                kids_if_u_does_not_buy = merge(kids_if_u_does_not_buy, child_res_0)
                
                kids_if_u_buys = merge(kids_if_u_buys, child_res_1)
                
            res_0 = [-float('inf')] * (budget + 1)
            
            res_1 = [-float('inf')] * (budget + 1)
            
            p_full = present[u]
            p_half = present[u] // 2
            prof_full = future[u] - p_full
            prof_half = future[u] - p_half
            
            for c in range(budget + 1):
                val_no_buy = kids_if_u_does_not_buy[c]
                
                if val_no_buy > res_0[c]: 
                    res_0[c] = val_no_buy

                if c >= p_full and kids_if_u_buys[c - p_full] != -float('inf'):
                    val_buy_full = kids_if_u_buys[c - p_full] + prof_full
                    if val_buy_full > res_0[c]: 
                        res_0[c] = val_buy_full

                if val_no_buy > res_1[c]: 
                    res_1[c] = val_no_buy

                if c >= p_half and kids_if_u_buys[c - p_half] != -float('inf'):
                    val_buy_half = kids_if_u_buys[c - p_half] + prof_half
                    if val_buy_half > res_1[c]: res_1[c] = val_buy_half
            
            return res_0, res_1
        final_dp, _ = dfs(0)
        
        return max(0, max(final_dp))