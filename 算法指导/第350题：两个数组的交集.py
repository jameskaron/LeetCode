# 给定两个数组，编写一个函数来计算它们的交集。
# 示例 1:
# 输入: nums1 = [1,2,2,1], nums2 = [2,2]
# 输出: [2,2]

# 示例 2:
# 输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# 输出: [4,9]
import collections
from typing import List

class Solution:
    def intersect(self, num1: List[int], num2: List[int]):
        if len(num1) > len(nums2):
            return self.intersect(num2, num1)

        m = collections.Counter()
        for num in num1:
            m[num] += 1

        intersection = list()
        for num in num2:
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)

        return intersection

    def intersect2(self, num1: List[int], num2: List[int]):
        num1 = sorted(num1)
        num2 = sorted(num2)
        i = 0
        j = 0
        k = 0
        result = []
        while i < len(num1):
            if j < len(num2):
                if num1[i] > num2[j]:
                    j += 1
                elif num1[i] < num2[j]:
                    i += 1
                else:
                    result.append(num1[i])
                    i += 1
                    j += 1
                    k += 1
        return result



s = Solution()
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
nums3 = [4,9,5]
nums4 = [9,4,9,8,4]
# print(s.intersect(nums3, nums4))
print(s.intersect2(nums1, nums2))