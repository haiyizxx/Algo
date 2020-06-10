package problem.tree;

import java.util.List;
import java.util.LinkedList;
import java.util.ArrayList;
import java.util.Queue;
import algorithm.TreeNode;


public class LC102_BinaryTreeLevelOrderTraversal {

    public static List<List<Integer>> recursion(TreeNode root) {
        List<List<Integer>> res = new LinkedList<>();
        class Traversal {
            private void run(TreeNode node, int level) {
                if (res.size() == level)
                    res.add(new ArrayList<>());
                res.get(level).add(node.val);
                if (node.left != null)
                    run(node.left, level + 1);
                if (node.right != null)
                    run(node.right, level + 1);

            }
        }
        new Traversal().run(root, 0);
        return res;
    }

    public static List<List<Integer>> iterationBFS(TreeNode root) {
        List<List<Integer>> res = new LinkedList<>();
        Queue<TreeNode> queue = new LinkedList<>();
        if (root == null)
            return res;
        queue.add(root);
        int level = 0;
        while (!queue.isEmpty()) {

            res.add(new ArrayList<Integer>());
            int level_length = queue.size();
            for (int i = 0; i < level_length; i++) {
                TreeNode node = queue.remove();
                res.get(level).add(node.val);
                if (node.left != null)
                    queue.add(node.left);
                if (node.right != null)
                    queue.add(node.right);

            }
            level++;
        }
        return res;

    }
}
