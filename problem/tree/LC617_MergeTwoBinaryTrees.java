package problem.tree;

import algorithm.TreeNode;
import java.util.Stack;

public class LC617_MergeTwoBinaryTrees {

    public static TreeNode recursive(TreeNode t1, TreeNode t2) {
        if (t1 == null)
            return t2;
        if (t2 == null)
            return t1;
        t1.val += t2.val;
        t1.left = recursive(t1.left, t2.left);
        t1.right = recursive(t1.right, t2.right);
        return t1;
    }

    public static TreeNode iterative(TreeNode t1, TreeNode t2) {
        if (t1 == null)
            return t2;
        Stack<TreeNode[]> stack = new Stack<>();
        stack.push(new TreeNode[] {t1, t2});
        while (!stack.isEmpty()) {
            TreeNode[] t = stack.pop();
            if (t[0] == null || t[1] == null)
                continue;
            t[0].val += t[1].val;
            if (t[0].left == null)
                t[0].left = t[1].left;
            else
                stack.add(new TreeNode[] {t[0].left, t[1].left});

            if (t[0].right == null)
                t[0].right = t[1].right;
            else
                stack.add(new TreeNode[] {t[0].right, t[1].right});

        }
        return t1;
    }
}
