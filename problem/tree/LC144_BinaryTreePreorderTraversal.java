package problem;

import algorithm.TreeNode;
import apple.laf.JRSUIUtils.Tree;
import java.util.LinkedList;
import java.util.List;

/*
 * How to traverse the tree There are two general strategies to traverse a tree:
 */
// 1. Breadth First Search (BFS)
// We scan through the tree level by level, following the order of height, from top to
// bottom. The nodes on higher level would be visited before the ones with lower levels.
//
// 2. Depth First Search
// one would start from a root and reach all the way down to certain leaf, and then back to root to
// reach another branch.
// The DFS strategy can further be distinguished as preorder, inorder, and postorder
// DFS PostOrder: Bottom -> Top Left -> Right
// DFS Preorder: Top -> Bottom Left -> Right
// DFS Inorder: Left -> Node -> Right
// BFS: Left -> Right Top -> Bottom

public class LC144_BinaryTreePreorderTraversal {

    public static List<Integer> recursion(TreeNode root) {
        List<Integer> res = new LinkedList<>();
        class Traversal {
            private void run(TreeNode node) {
                if (node == null)
                    return;
                res.add(node.val);
                run(node.left);
                run(node.right);
            }
        }
        new Traversal().run(root);
        return res;
    }

    /*
     * 
     * Time complexity : we visit each node exactly once, thus the time complexity is O(N), where NN
     * is the number of nodes, i.e. the size of tree. Space complexity
     * 
     * Space complexity: depending on the tree structure, we could keep up to the entire tree,
     * therefore, the space complexity is O(N).
     */
    public static List<Integer> iterationDFSPreorder(TreeNode root) {
        LinkedList<TreeNode> stack = new LinkedList<>();
        List<Integer> res = new LinkedList<>();

        if (root == null)
            return res;

        stack.add(root);
        while (!stack.isEmpty()) {
            TreeNode node = stack.pollLast();
            res.add(node.val);
            if (node.right != null)
                stack.add(node.right);
            if (node.left != null)
                stack.add(node.left);
        }
        return res;
    }
}
