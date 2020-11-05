# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minimal_exec_time(self, root):
        total, parallel = self.get_total_and_parallel(root)
        return total - parallel

    def get_total_and_parallel(self, root):
        # 判断如果节点为None则返回0(左节点), 0(右节点)
        if root is None:
            return 0, 0

        # 递归计算左右子树的总耗时以及最大并行时间
        t_left, p_left = self.get_total_and_parallel(root.left)
        t_right, p_right = self.get_total_and_parallel(root.right)
        total = root.val + t_left + t_right

        # 假定左子树的耗时一定比右子树耗时大，如果不是则交换
        if t_left < t_right:
            t_left, t_right = t_right, t_left
            p_left, p_right = p_right, p_left

        # 判断左右子树能否达到最大并行时间(t_left + t_right) / 2
        # 此处(a+b)/2，求和除2取均值若a,b很大，则会造成a+b内存溢出，可修改成b+(a-b)/2
        if t_left - 2 * p_left <= t_right:
            return total, t_right + (t_left - t_right) / 2
        else:
            return total, p_left + t_right