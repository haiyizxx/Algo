package problem.tree;

import algorithm.TreeNode;

public class LC669_TrimBST {
    public static TreeNode recursive(TreeNode root, int L, int R) {
        // Preorder
        if (root == null)
            return root;
        if (root.val > R)
            return recursive(root.left, L, R);
        if (root.val < L)
            return recursive(root.right, L, R);
        root.left = recursive(root.left, L, R);
        root.right = recursive(root.right, L, R);
        return root;
    }
}
