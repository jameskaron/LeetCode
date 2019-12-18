# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
class Solution:
    def moveZeroes(self, nums: list) -> list:
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                if i != j:
                    nums[j] = nums[i]
                    nums[i] = 0
                j += 1
        return nums


s = Solution()
data = [0,1,0,3,12]
# data = [0,1,0,0,9,2,3,12]
print(s.moveZeroes(data))