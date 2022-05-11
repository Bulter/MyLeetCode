"""
找出数组中重复的数字。

在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。
数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。

请找出数组中任意一个重复的数字。

输入：
[2, 3, 1, 0, 2, 5, 3]

输出：
2 或 3 

思路：
1. 定义一个list用来计数(list耗时高，不知为啥)
2. 定义个set用来计数，通过向集合中add（如果集合有元素只会add失败，不会报异常），然后计算长度作为标识

3. 以上思路空间复杂度过高，读题可发现长度为n的数组nums取值范围为[0, n-1]，也就是说一个索引值（比如2）可以在nums找到多个值
  所以可以利用特点进行排序

"""
from typing import List


class Solution:
     def findRepeatNumber(self, nums: List[int]) -> int:
        """
        优化空间为 O(1)
        
        """
        i = 0
        while i < len(nums):
            if i == nums[i]:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            # 如果不相等，则交换位置
            # 注意此处不能写成nums[i], nums[nums[i]] = nums[nums[i]], nums[i]
            # 因为赋值从左到右会先将nums[i]的值赋好，这样nums[nums[i]]取到的就不是原来的值了
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
            
    
    #  def findRepeatNumber(self, nums: List[int]) -> int:
    #     """
    #     set 计数
        
    #     """
    #     count_set = set()
    #     for i in range(len(nums)):
    #         count_set.add(nums[i])
    #         if len(count_set) != i + 1:
    #             return nums[i]
    
    # def findRepeatNumber(self, nums: List[int]) -> int:
    #     """
    #     弃用，尽管通过测试，但是耗时太长达8s
    #     """
    #     cout_list = []
    #     for n in nums:
    #         if n in cout_list:
    #             return n
    #         else:
    #             cout_list.append(n)
    

if __name__ == "__main__":
    nums = [2, 3, 1, 0, 2, 5, 3]
    print(Solution().findRepeatNumber(nums))