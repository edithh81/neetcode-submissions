class Solution:
    def isValid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def mark(self, grid, i, j, n, m):
        grid[i][j] = '0'
        dx = [-1, 0, 0, 1]
        dy = [0, 1, -1, 0]
        for k in range(4):
            i1, j1 = i + dx[k], j + dy[k]
            if self.isValid(i1, j1, n, m) and (grid[i1][j1] == '1'):
                self.mark(grid, i1, j1, n, m)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        n, m = len(grid), len(grid[0])
        for i in range(n):
            for j in range(m):
                if (grid[i][j] == '1'):
                    count += 1
                    self.mark(grid, i, j, n, m)

        return count