package problem.tree;

import algorithm.TreeNode;

public class LC543_DiameterOfBinaryTree {
    private int ans = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        if (root == null)
            return 0;
        recursive(root);
        return ans;
    }

    private int recursive(TreeNode node) {
        if (node == null)
            return -1;
        int left_tree = 1 + recursive(node.left);
        int right_tree = 1 + recursive(node.right);
        int sub_max = Math.max(left_tree, right_tree);
        ans = Math.max(ans, left_tree + right_tree);
        return sub_max;
    }
}}
