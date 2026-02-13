class Solution:
    def longestBalanced(self,s: str) -> int:
    
        max_len = 0
        current_run = 0
        for i in range(len(s)):
            if i>0 and s[i] == s[i-1]:
                current_run += 1
            else:
                current_run=1
            max_len = max(max_len, current_run)

        
        def solve_two_chars(char1, char2, forbidden):
            nonlocal max_len
            seen = {0: -1}
            diff = 0
            
            for i, char in enumerate(s):
                if char == forbidden:
                    seen = {0: i}
                    diff = 0
                    continue
                
                if char == char1:
                    diff += 1
                elif char == char2:
                    diff -= 1

                if diff in seen:
                    max_len = max(max_len, i - seen[diff])
                else:
                    seen[diff] = i

        solve_two_chars('a', 'b', 'c')
        solve_two_chars('b', 'c', 'a')
        solve_two_chars('a', 'c', 'b')

        
        seen_triple = {(0, 0): -1}
        a = b = c = 0
        
        for i, char in enumerate(s):
            if char == 'a': a += 1
            elif char == 'b': b += 1
            elif char == 'c': c += 1
            
            diff1 = a - b
            diff2 = b - c
            key = (diff1, diff2)
            
            if key in seen_triple:
                max_len = max(max_len, i - seen_triple[key])
            else:
                seen_triple[key] = i
                
        return max_len