package algorithm;

import java.util.*;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;

    TreeNode() {
    }

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }


    // 1
    // / \
    // 2 3
    // / \
    // 4 5
    // Preoder(root, left, right): 1 2 4 5 3
    // Inorder(left, root, right): 4 2 5 1 3
    // Postorder(left, right, root) 4 5 2 3 1

    // For itertion
    // If use stack for preorder, push right node first, then left.


    public static void preorder(TreeNode root) {
        if (root == null)
            return;
        // Do sth. with val
        preorder(root.left);
        preorder(root.right);

    }

    public static void inorder(TreeNode root) {
        if (root == null)
            return;
        preorder(root.left);
        // Do sth. with val
        preorder(root.right);
    }

    public static void postorder(TreeNode root) {
        if (root == null)
            return;
        preorder(root.left);
        preorder(root.right);
        // Do sth. with val
    }

    // BFS use a queue, FIFO For every node removed from the queuequeue, we add all its children to
    // the back of the same queuequeue.

    public static void breadthFirstSearch(TreeNode root) {

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);
        while (!queue.isEmpty()) {
            Queue<TreeNode> temp = new LinkedList<>();
            while (!queue.isEmpty()) {
                TreeNode n = queue.remove();
                if (n.left != null)
                    temp.add(n.left);
                if (n.right != null)
                    temp.add(n.right);
            }
            queue = temp;
        }
    }
}
