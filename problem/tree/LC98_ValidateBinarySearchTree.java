package problem.tree;

import algorithm.TreeNode;
import java.util.*;

public class LC98_ValidateBinarySearchTree {
    public boolean isValidBST(TreeNode root) {
        return recursive(root, null, null);
    }

    private boolean recursive(TreeNode node, Integer left, Integer right) {
        if (node == null)
            return true;
        int val = node.val;
        if (left != null && val <= left)
            return false;
        if (right != null && val >= right)
            return false;

        return recursive(node.left, left, val) && recursive(node.right, val, right);
    }


    public boolean isValidBSTInorder(TreeNode root) {

        Stack<TreeNode> stack = new Stack();
        double inorder = -Double.MAX_VALUE;
        TreeNode node = root;
        while (!stack.isEmpty() || node != null) {
            while (node != null) {
                stack.push(node);
                node = node.left;
            }
            node = stack.pop();
            if (node.val <= inorder)
                return false;
            inorder = node.val;
            node = node.right;
        }
        return true;
    }

}
