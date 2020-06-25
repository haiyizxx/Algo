package problem.tree;

import algorithm.TreeNode;

public class LC124_BinaryTreeMaxPathSum {
    // Similar to LC 687, 543
    int max_sum = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        recursive(root);
        return max_sum;
    }

    private int recursive(TreeNode node) {
        if (node == null)
            return 0;
        int left = Math.max(recursive(node.left), 0);
        int right = Math.max(recursive(node.right), 0);
        int new_path = node.val + left + right;
        max_sum = Math.max(max_sum, new_path);
        return node.val + Math.max(left, right);

    }
}
