package problem.tree;

import algorithm.TreeNode;
import java.util.List;
import java.util.LinkedList;


public class LC94_BinaryTreeInorderTraversal {
    public static List<Integer> recursive(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        class Traversal {
            private void run(TreeNode node) {
                if (node == null)
                    return;

                run(node.left);
                res.add(node.val);
                run(node.right);
            }
        }
        new Traversal().run(root);
        return res;
    }

    public static List<Integer> iterationDFS(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        LinkedList<TreeNode> stack = new LinkedList<>();
        if (root == null)
            return res;
        TreeNode curr = root;
        while (!stack.isEmpty() || curr != null) {
            while (curr != null) {
                stack.add(curr);
                curr = curr.left;
            }
            curr = stack.pollLast();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}
