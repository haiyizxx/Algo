package problem;

import algorithm.UnionFind;
import java.util.LinkedList;
import java.util.List;

class Pair<U, V> {
    public U first;
    public V second;

    public Pair(U first, V second) {
        this.first = first;
        this.second = second;
    }
}

class SurrendedRegions {
    private static final char O = 'O';
    private static final char X = 'X';
    private int rows;
    private int cols;

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
                        int y = j + d[k][1];

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

    // Solve use DFS/BFS
    public void solve2(char[][] board) {
        if (board == null || board.length == 0)
            return;
        rows = board.length;
        cols = board[0].length;

        List<Pair<Integer, Integer>> borders = new LinkedList<Pair<Integer, Integer>>();
        // Construct list of border cells
        for (int r = 0; r < rows; r++) {
            borders.add(new Pair(r, 0));
            borders.add(new Pair(r, cols - 1));
        }
        for (int c = 0; c < cols; c++) {
            borders.add(new Pair(0, c));
            borders.add(new Pair(rows - 1, c));
        }
        // Step 2
        for (Pair<Integer, Integer> pair : borders)
            DFS(board, pair.first, pair.second);
        // Step 3
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (board[r][c] == 'O')
                    board[r][c] = 'X';
                if (board[r][c] == 'E')
                    board[r][c] = 'O';
            }
        }
    }

    private void DFS(char[][] board, int row, int col) {
        if (row < 0 || row >= rows || col < 0 || col >= cols)
            return;

        if (board[row][col] != 'O')
            return;

        board[row][col] = 'E';
        int[][] d = new int[][] { { 1, 0 }, { 0, 1 }, { 0, -1 }, { -1, 0 } };

        for (int k = 0; k < 4; k++) {
            int x = row + d[k][0];
            int y = col + d[k][1];

            DFS(board, x, y);
        }
    }

    private void BFS(char[][] board, int r, int c) {
        LinkedList<Pair<Integer, Integer>> queue = new LinkedList<>();
        queue.offer(new Pair<>(r, c));
        while (!queue.isEmpty()) {
            Pair<Integer, Integer> p = queue.pollFirst();
            int row = p.first, col = p.second;
            if (board[row][col] != 'O')
                continue;
            board[row][col] = 'E';

            if (col < cols - 1)
                queue.offer(new Pair<>(row, col + 1));
            if (col > 0)
                queue.offer(new Pair<>(row, col - 1));
            if (row < rows - 1)
                queue.offer(new Pair<>(row + 1, col));
            if (row > 0)
                queue.offer(new Pair<>(row - 1, col));
        }
    }
}