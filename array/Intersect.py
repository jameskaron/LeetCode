# 给定两个数组，编写一个函数来计算它们的交集
class Solution:
    def intersect(self, nums1: list, nums2: list) -> list:
        ints = []
        for i1 in nums1:
            if i1 in nums2:
                ints.append(i1)
        return ints


s = Solution()
nums1 = [1,2,2,1]
nums2 = [2]
# nums1 = [4,9,5]
# nums2 = [9,4,9,8,4]
print(s.intersect(nums1, nums2))