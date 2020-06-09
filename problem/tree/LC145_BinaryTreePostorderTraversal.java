package problem.tree;

import algorithm.TreeNode;
import java.util.List;
import java.util.LinkedList;


public class LC145_BinaryTreePostorderTraversal {
    public static List<Integer> recursive(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        class Traversal {
            private void run(TreeNode node) {
                if (node == null)
                    return;
                run(node.left);
                run(node.right);
                res.add(node.val);
            }
        }
        new Traversal().run(root);
        return res;
    }

    // [1, null, 2, 3]
    // [1]
    // [2, 1]
    // [3, 2, 1]
    public static List<Integer> iterationDFS(TreeNode root) {
        LinkedList<Integer> res = new LinkedList<>();
        LinkedList<TreeNode> stack = new LinkedList<>();
        if (root == null)
            return res;

        stack.add(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pollLast();
            res.addFirst(node.val);
            if (node.left != null)
                stack.add(node.left);
            if (node.right != null)
                stack.add(node.right);
        }
        return res;
    }
}
