# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有满足条件且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。

# 示例：
#
# 给定数组 nums = [-1, 0, 1, 2, -1, -4]，
#
# 满足要求的三元组集合为：
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]
#
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        if not nums or n < 3:
            return []
        # 1. 排序
        nums.sort()
        for i in range(n):
            if nums[i] > 0:
                return res
            # 判断两数是否相同, 相同则跳过
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2. 双指针
            L = i + 1
            R = n - 1
            while L < R:
                # 找到结果
                if nums[i] + nums[L] + nums[R] == 0:
                    res.append([nums[i], nums[L], nums[R]])
                    # 跳过相同
                    while L < R and nums[L] == nums[L + 1]:
                        L += 1
                    while L < R and nums[R] == nums[R - 1]:
                        R -= 1
                    L += 1
                    R -= 1
                # 结果>0, 移动R指针,减少结果
                elif nums[i] + nums[L] + nums[R] > 0:
                    R -= 1
                # 结果<0, 移动L指针,增加结果
                elif nums[i] + nums[L] + nums[R] < 0:
                    L += 1
        return res


if __name__ == '__main__':
    s = Solution()
    nums_1 = [-1, 0, 1, 2, -1, -4]
    # nums_2 = [-1, 0, 1, 2, -1, -4]
    assert s.threeSum(nums_1) == [[-1, 0, 1], [-1, -1, 2]] or [[-1, -1, 2], [-1, 0, 1]]
    # assert s.threeSum(nums_2) == [[-1, 0, 1], [-1, -1, 2]]
