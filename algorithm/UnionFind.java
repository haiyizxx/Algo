package algorithm;

public class UnionFind {
    private int count;
    // Parent of each node
    private int[] parent;
    // Size of each node
    private int[] size;

    public UnionFind(int n) {
        count = n;
        size = new int[n];
        parent = new int[n];
        for (int i = 0; i < n; i++) {
            parent[i] = i;
            size[i] = 1;
        }
    }

    // Find root of a node
    private int find(int x) {
        while (parent[x] != x) {
            // Compress the root
            parent[x] = parent[parent[x]];
            x = parent[x];
        }
        return x;

    }

    // Union node p and node q
    public void union(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);

        if (rootP == rootQ)
            return;
        // Link small tree under large tree
        if (size[rootP] > size[rootQ]) {
            parent[rootQ] = rootP;
            size[rootP] += size[rootQ];
        } else {
            parent[rootP] = rootQ;
            size[rootQ] += size[rootP];
        }
        count--;
    }

    public boolean connected(int p, int q) {
        int rootP = find(p);
        int rootQ = find(q);
        return rootP == rootQ;
    }

    public int count() {
        return count;
    }
}