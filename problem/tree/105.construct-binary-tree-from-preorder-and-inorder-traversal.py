#
# @lc app=leetcode id=105 lang=python3
#
# [105] Construct Binary Tree from Preorder and Inorder Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:               # 1.root  5.left  6.right
    # preorder: node left right  [  3,  9,  8,  20,  15,  7]
    # inorder: left node right   [  8,  9,  3,  15,  20,  7]
    #                           3.left    2.root   4.right
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        # root = TreeNode(preorder[0])
        d = {}

        for i in range(len(preorder)):
            d[inorder[i]] = i

        return self.helper(preorder, inorder, 0, 0, len(inorder)-1, d)

    def helper(self, preorder, inorder, pre_start, in_start, in_end, d):
        if pre_start >= len(preorder) or in_start > in_end:
            return None

        root = TreeNode(preorder[pre_start])
        root_idx = d[preorder[pre_start]]
        # pre_start+1 is the start of left tree in preorder

        # print(f'root_idx： {root_idx}')
        # print(f'preorder right sub tree: {pre_start+(root_idx-in_start+1)}')
        # print('--------')
        root.left = self.helper(
            preorder, inorder, pre_start+1, in_start, root_idx-1, d)

        # pre_start + (root_index - in_start + 1) -> number of left subtree in in order
        # e.g. root of left subtree 9's index is 1 (inorder)
        #      right subtree index is 0 + 2 - 0 + 1 = 3
        root.right = self.helper(
            preorder,
            inorder,
            pre_start+(root_idx-in_start+1),
            root_idx+1,
            in_end,
            d
        )

        return root

# @lc code=end
