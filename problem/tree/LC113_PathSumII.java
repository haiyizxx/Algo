package problem.tree;

import java.util.*;
import algorithm.TreeNode;

public class LC113_PathSumII {
    public static List<List<Integer>> pathSum(TreeNode root, int sum) {
        List<List<Integer>> pathList = new ArrayList<>();
        List<Integer> pathNodes = new ArrayList<>();

        recursive(root, sum, pathNodes, pathList);
        return pathList;
    }

    private static void recursive(TreeNode node, int remainSum, List<Integer> pathNodes,
            List<List<Integer>> pathList) {
        if (node == null)
            return;
        pathNodes.add(node.val);
        if (remainSum == node.val && node.left == null && node.right == null)
            pathList.add(new ArrayList<>(pathNodes));
        else
            recursive(node.left, remainSum - node.val, pathNodes, pathList);
        recursive(node.right, remainSum - node.val, pathNodes, pathList);
        // We need to pop the node once we are done processing it's subtree
        pathNodes.remove(pathNodes.size() - 1);
    }
}
