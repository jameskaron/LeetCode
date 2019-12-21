# 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。
#
# 你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
#
# 示例:
#
# 给定 nums = [2, 7, 11, 15], target = 9
#
# 因为 nums[0] + nums[1] = 2 + 7 = 9
# 所以返回 [0, 1]
class Solution:
    # 暴力破解(超时)
    def twoSum_one(self, nums: list, target: int) -> list:
        res = []
        j = 0
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if i != j:
                    if nums[i] + nums[j] == target:
                        res.append(i)
                        res.append(j)
                        return res

    # 解题关键主要是想找到 num2 = target - num1，是否也在 list 中，那么就需要运用以下两个方法：
    # num2 in nums，返回 True 说明有戏
    # nums.index(num2)，查找 num2 的索引
    def twoSum_two(self, nums: list, target: int) -> list:
        res = []
        for i in range(len(nums)):
            num2 = target - nums[i]
            if num2 in nums:
                num2_idx = nums.index(num2)
            if num2 in nums and i != num2_idx:
                res.append(i)
                res.append(num2_idx)
                res.sort()
                return res

    # 参考了大神们的解法，通过哈希来求解，这里通过字典来模拟哈希查询的过程。
    # 个人理解这种办法相较于方法一其实就是字典记录了 num1 和 num2 的值和位置，而省了再查找 num2 索引的步骤
    # 通过字典的方法，查找效率快很多，执行速度大幅缩短
    def twoSum_three(self, nums: list, target: int) -> list:
        res_map = {}
        for idx, item in enumerate(nums):
            res_map[item] = idx
        for i, num in enumerate(nums):
            j = res_map.get(target - num)
            if j is not None and i != j:
                return [i, j]


s = Solution()
data_1 = [2, 7, 11, 15]
# print(s.twoSum_two(data_1, 9))
# data_2 = [3,2,3]
print(s.twoSum_three(data_1, 9))
