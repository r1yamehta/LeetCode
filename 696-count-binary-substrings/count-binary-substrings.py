class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        prev_run_length = 0
        curr_run_length = 1
        total_substrings = 0

        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                curr_run_length += 1
            else:
                total_substrings += min(prev_run_length, curr_run_length)
                prev_run_length = curr_run_length
                curr_run_length = 1
                
        total_substrings += min(prev_run_length, curr_run_length)

        return total_substrings