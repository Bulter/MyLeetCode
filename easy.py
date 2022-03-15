from typing import List


class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        """
            两数之和：
                给定一个整数数组 nums 和一个整数目标值 target，
                请你在该数组中找出和为目标值 target  的那两个整数，
                并返回它们的数组下标。
            思路：
                对于 x ，找 target-x 是否在数组中
        """
        # 1. 暴力穷举
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
                
        # 2. 哈希表
        hash_table = dict()
        for i, num in enumerate(nums):
            if target - num in hash_table:
                return [hash_table[target - num], i]
            hash_table[num] = i
        
        return []
        