package problem.tree;

import algorithm.TreeNode;
import java.util.*;

public class LC100_SameTree {
    public static boolean recursive(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;
        if (p == null || q == null)
            return false;
        if (p.val != q.val)
            return false;
        return recursive(p.left, q.left) && recursive(p.right, q.right);
    }

    public static boolean iterative(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;
        Queue<TreeNode> queueP = new LinkedList<>();
        Queue<TreeNode> queueQ = new LinkedList<>();
        queueP.add(p);
        queueQ.add(q);

        while (!queueP.isEmpty()) {
            TreeNode nodeP = queueP.remove();
            TreeNode nodeQ = queueQ.remove();
            if (!check(nodeP, nodeQ))
                return false;
            if (nodeP != null) {
                if (nodeP.left == null && nodeQ.left != null)
                    return false;

                queueP.add(nodeP.left);
                queueQ.add(nodeQ.left);

                if (nodeP.right == null && nodeQ.right != null)
                    return false;

                queueP.add(nodeP.right);
                queueQ.add(nodeQ.right);
            }

        }


        return true;
    }

    private static boolean check(TreeNode p, TreeNode q) {
        if (p == null && q == null)
            return true;
        if (p == null || q == null)
            return false;
        if (p.val != q.val)
            return false;
        return true;
    }
}
