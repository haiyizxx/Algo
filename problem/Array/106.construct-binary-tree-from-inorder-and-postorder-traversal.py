#
# @lc app=leetcode id=106 lang=python3
#
# [106] Construct Binary Tree from Inorder and Postorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        d = {}
        for i in range(len(inorder)):
            d[inorder[i]] = i
        return self.helper(inorder, postorder, len(postorder)-1, 0, len(inorder)-1, d)

    def helper(self, inorder, postorder, post_idx, inorder_start, inorder_end, d):
        if post_idx < 0 or inorder_start > inorder_end:
            return None

        root = TreeNode(postorder[post_idx])
        root_idx = d[postorder[post_idx]]

        left_inorder_start = inorder_start
        left_inorder_end = root_idx-1

        right_inorder_start = root_idx+1
        right_inorder_end = inorder_end

        root.right = self.helper(
            inorder,
            postorder,
            post_idx-1,
            right_inorder_start,
            right_inorder_end,
            d
        )

        root.left = self.helper(
            inorder,
            postorder,
            post_idx - (inorder_end-root_idx + 1),
            left_inorder_start,
            left_inorder_end,
            d
        )
        return root
# @lc code=end
