
class Solution:
    # 朴素线性查找:遍历
    # 循环不变式: 在下一次搜索之前,搜索过的整数中没有重复的整数。
    def containsDuplicate_one(self, nums: list) -> bool:
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] == nums[i]:
                    return True
        return False

    # 排序:如果存在重复元素，排序后它们应该相邻
    def containsDuplicate_two(self, nums: list) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                return True
        return False

    # 哈希表:利用支持快速搜索和插入操作的动态数据结构。
    def containsDuplicate_three(self, nums: list) -> bool:
        nums_set = set()
        for item in nums:
            if nums_set.__contains__(item):
                return True
            nums_set.add(item)
        return False


solution = Solution()
data = [1, 2, 3, 1]
print(solution.containsDuplicate_one(data))
# print(solution.containsDuplicate_two(data))
# print(solution.containsDuplicate_three(data))
