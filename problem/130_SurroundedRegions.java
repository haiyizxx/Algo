package problem;

import algorithm.UnionFind;

class SurrendedRegions {
    static final char O = 'O';
    static final char X = 'X';

    public void solve(char[][] board) {
        if (board.length == 0)
            return;
        int m = board.length;
        int n = board[0].length;
        UnionFind uf = new UnionFind(n * m + 1);
        int dummy = m * n;
        // Link first row and last row 'O' to dummy
        for (int i = 0; i < n; i++) {
            if (board[0][i] == O) {
                uf.union(i, dummy);
            }
            if (board[m - 1][i] == 0) {
                uf.union((m - 1) * n + i, dummy);
            }
        }
        // Link first and last col 'O' to dummy
        for (int i = 0; i < m; i++) {
            if (board[i][0] == O) {
                uf.union(i * n, dummy);
            }
            if (board[i][n - 1] == O) {
                uf.union(i * n + n - 1, dummy);
            }
        }

        int[][] d = new int[][] { { 1, 0 }, { 0, 1 }, { 0, -1 }, { -1, 0 } };

        for (int i = 1; i < m - 1; i++) {
            for (int j = 1; j < n - 1; j++) {
                if (board[i][j] == O)
                    for (int k = 0; k < 4; k++) {
                        int x = i + d[k][0];
                        int y = i + d[k][1];

                        if (board[x][y] == O)
                            uf.union(x * n + y, i * n + j);
                    }
            }
        }
        // Only 'O' link to dummy won't be linked
        for (int i = 1; i < m - 1; i++)
            for (int j = 1; j < n - 1; j++)
                if (!uf.connected(i * n + j, dummy))
                    board[i][j] = X;

    }
}