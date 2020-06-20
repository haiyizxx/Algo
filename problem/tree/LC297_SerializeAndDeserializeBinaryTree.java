package problem.tree;

import java.util.*;
import algorithm.TreeNode;

public class LC297_SerializeAndDeserializeBinaryTree {
    // Encodes a tree to a single string.
    public static String serializeDFS(TreeNode root) {
        return serializeDFS(root, "");
    }

    private static String serializeDFS(TreeNode root, String str) {
        if (root == null) {
            str += "null,";
        } else {
            str += String.valueOf(root.val) + ",";
            str = serializeDFS(root.left, str);
            str = serializeDFS(root.right, str);
        }
        return str;
    }

    // Decodes your encoded data to tree.
    public static TreeNode deserializeDFS(String data) {
        String[] data_array = data.split(",");
        List<String> data_list = new LinkedList<String>(Arrays.asList(data_array));
        return deserializeDFS(data_list);
    }

    public static TreeNode deserializeDFS(List<String> data_list) {
        if (data_list.get(0).equals("null")) {
            data_list.remove(0);
            return null;
        }

        TreeNode root = new TreeNode(Integer.valueOf(data_list.get(0)));
        data_list.remove(0);
        root.left = deserializeDFS(data_list);
        root.right = deserializeDFS(data_list);
        return root;
    }
}
