package algorithm;

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
}
