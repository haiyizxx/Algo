package problem.tree;

import algorithm.TreeNode;

public class LC110_BalancedBinaryTree {
    public static boolean topDown(TreeNode root) {
        if (root == null)
            return true;
        return topDown(root.left) && topDown(root.right)
                && Math.abs(recursive(root.left) - recursive(root.right)) < 2;


    }

    private static int recursive(TreeNode node) {
        if (node == null)
            return -1;
        return 1 + Math.max(recursive(node.left), recursive(node.right));
    }

    public static boolean bottomUp(TreeNode root) {
        return getHeight(root) != -1;
    }

    private static int getHeight(TreeNode node) {
        if (node == null)
            return 0;

        int left = getHeight(node.left);
        int right = getHeight(node.right);

        if ((left == -1) || (right == -1) || (Math.abs(left - right) > 1))
            return -1;
        return Math.max(left, right) + 1;

    }
}
