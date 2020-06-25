package problem.tree;

import algorithm.TreeNode;
import java.util.*;

public class LC449_SerializeAndDeserializeBST {
    // Relate to LC 297
    // Solution 1
    public String serializePostOrder(TreeNode root) {
        StringBuilder sb = postorder(root, new StringBuilder());
        if (sb.length() > 0)
            sb.deleteCharAt(sb.length() - 1);
        return sb.toString();
    }

    private StringBuilder postorder(TreeNode node, StringBuilder sb) {
        if (node == null)
            return sb;
        postorder(node.left, sb);
        postorder(node.right, sb);
        sb.append(node.val);
        sb.append(' ');
        return sb;
    }

    // Decodes your encoded data to tree.
    public TreeNode deserializePostOrder(String data) {
        if (data.isEmpty())
            return null;
        ArrayDeque<Integer> nums = new ArrayDeque<Integer>();
        for (String s : data.split("\\s+"))
            nums.add(Integer.valueOf(s));
        return dePostorderHelper(Integer.MIN_VALUE, Integer.MAX_VALUE, nums);
    }

    private TreeNode dePostorderHelper(Integer lower, Integer upper, ArrayDeque<Integer> nums) {
        if (nums.isEmpty())
            return null;
        int val = nums.getLast();
        if (val < lower || val > upper)
            return null;
        nums.removeLast();
        TreeNode root = new TreeNode(val);
        root.right = dePostorderHelper(val, upper, nums);
        root.left = dePostorderHelper(lower, val, nums);
        return root;
    }


    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        preorder(root, sb);
        return sb.toString();
    }

    private void preorder(TreeNode node, StringBuilder sb) {
        if (node == null)
            return;
        sb.append(intToStr(node.val));
        preorder(node.left, sb);
        preorder(node.right, sb);
    }

    private static String intToStr(int x) {
        char[] chars = new char[2];
        for (int i = 1; i >= 0; i--)
            chars[1 - i] = (char) ((x >> (16 * i)) & 0xffff);
        return new String(chars);
    }

    // Decodes your encoded data to tree.
    public TreeNode deserialize(String data) {
        if (data.isEmpty())
            return null;
        Queue<Integer> q = new LinkedList<>();
        for (int i = 0; i < data.length(); i += 2) {
            String curr = data.substring(i, i + 2);
            q.offer(strToInt(curr));
        }
        return deDFS(q);
    }

    private static int strToInt(String str) {
        int result = 0;
        for (char b : str.toCharArray()) {
            result = (result << 16) + (int) b;
        }
        return result;
    }

    private TreeNode deDFS(Queue<Integer> q) {
        if (q.size() == 0)
            return null;

        TreeNode root = new TreeNode(q.poll());
        Queue<Integer> left = new LinkedList<>();

        while (!q.isEmpty() && q.peek() < root.val) {
            left.offer(q.poll());
        }
        root.left = deDFS(left);
        root.right = deDFS(q);
        return root;
    }

}
