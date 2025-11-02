class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        # 0 = empty, 1 = wall, 2 = guard, 3 = guarded
        grid = [[0] * n for _ in range(m)]

        for r, c in walls:
            grid[r][c] = 1
        for r, c in guards:
            grid[r][c] = 2

        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        for r, c in guards:
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                while 0 <= nr < m and 0 <= nc < n:
                    if grid[nr][nc] in (1, 2): 
                        break
                    if grid[nr][nc] == 0: 
                        grid[nr][nc] = 3
                    nr += dr
                    nc += dc

        return sum(grid[i][j] == 0 for i in range(m) for j in range(n))
