package problem.tree;

import algorithm.TreeNode;
import java.util.LinkedList;

public class LC404_SumOfLeftLeaves {

    public static int iterationDFS(TreeNode root) {
        int res = 0;
        if (root == null)
            return res;

        LinkedList<TreeNode> stack = new LinkedList<>();
        stack.add(root);

        while (!stack.isEmpty()) {
            TreeNode node = stack.pollLast();
            if (node.left != null && node.left.left == null && node.left.right == null)
                res += node.left.val;

            if (node.right != null)
                stack.add(node.right);

            if (node.left != null)
                stack.add(node.left);

        }

        return res;
    }

    public int recursive(TreeNode root) {
        if (root == null)
            return 0;
        return processSubtree(root, false);


    }

    private int processSubtree(TreeNode node, boolean isLeft) {

        // Base case
        if (node.left == null && node.right == null)
            return isLeft ? node.val : 0;

        int total = 0;
        if (node.left != null)
            total += processSubtree(node.left, true);
        if (node.right != null)

            total += processSubtree(node.right, false);
        return total;
    }
}
